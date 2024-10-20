import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import pickle

# Helper function to load datasets
def load_data(file_path):
    return pd.read_csv(file_path, sep='\t')

# Step 1: Load the Datasets
train_data = load_data('train.tsv')
valid_data = load_data('valid.tsv')
test_data = load_data('test.tsv')

# Combine train and valid datasets for training
data = pd.concat([train_data, valid_data], ignore_index=True)

# Extract the relevant columns and handle missing values
X_train = data.iloc[:, 2].astype(str).fillna('')  # Ensure all values are strings
y_train = data.iloc[:, 1].map({
    'false': 0, 'half-true': 0, 'true': 1, 'mostly-true': 1
}).fillna(0).values  # Map labels and handle missing values

X_test = test_data.iloc[:, 2].astype(str).fillna('')  # Ensure all values are strings
y_test = test_data.iloc[:, 1].map({
    'false': 0, 'half-true': 0, 'true': 1, 'mostly-true': 1
}).fillna(0).values

# Step 2: Tokenize the Text Data
vocab_size = 10000  # Adjust as needed
max_len = 100  # Maximum length of sequences

tokenizer = Tokenizer(num_words=vocab_size, oov_token='<OOV>')
tokenizer.fit_on_texts(X_train)  # Fit tokenizer on the training data

# Convert text to padded sequences
X_train_sequences = tokenizer.texts_to_sequences(X_train)
X_train_padded = pad_sequences(X_train_sequences, maxlen=max_len, padding='post')

X_test_sequences = tokenizer.texts_to_sequences(X_test)
X_test_padded = pad_sequences(X_test_sequences, maxlen=max_len, padding='post')

# Step 3: Split Training Data for Validation
X_train_final, X_val, y_train_final, y_val = train_test_split(
    X_train_padded, y_train, test_size=0.2, random_state=42
)

# Step 4: Build the Model
model = Sequential([
    Embedding(vocab_size, 128, input_length=max_len),
    Bidirectional(LSTM(64, return_sequences=True)),
    Dropout(0.5),
    Bidirectional(LSTM(32)),
    Dense(1, activation='sigmoid')  # Binary classification: Fake or Real
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 5: Train the Model
model.fit(
    X_train_final, y_train_final,
    epochs=5, validation_data=(X_val, y_val), batch_size=32
)

# Step 6: Evaluate the Model on Test Data
test_loss, test_accuracy = model.evaluate(X_test_padded, y_test)
print(f"Test Loss: {test_loss}, Test Accuracy: {test_accuracy}")

# Step 7: Save the Model and Tokenizer
model.save('keras_model.h5')

with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
