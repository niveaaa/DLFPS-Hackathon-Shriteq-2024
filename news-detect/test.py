import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load the saved model
model = tf.keras.models.load_model('text_model.h5')

# Load the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def preprocess_text(text, max_len=100):
    """Convert input text to padded sequence."""
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=max_len, padding='post')
    print("Padded Sequence:", padded_sequence)  # Debugging
    return padded_sequence

def predict(text):
    """Predict if the news is fake or real."""
    processed_text = preprocess_text(text)
    prediction = model.predict(processed_text)
    print("Raw Prediction Output:", prediction)  # Debugging
    
    # Ensure correct prediction value
    score = prediction[0][0]
    label = "Fake News" if score < 0.5 else "Real News"
    confidence = np.round(score if score >= 0.5 else 1 - score, 2)
    return label, confidence

# Test with a sample text
text = "the sun is very hot"
label, confidence = predict(text)
print(f"Prediction: {label}, Confidence: {confidence}")
