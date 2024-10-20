import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle
import streamlit as st

# Load the trained model and tokenizer
model = load_model('text_model.h5')

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Function to preprocess input text
def preprocess_text(text, max_len=100):
    # Tokenize and pad the sequence
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_len)
    return padded_sequences

# Function to predict if text is fake or real
def predict(text):
    preprocessed_text = preprocess_text(text)
    prediction = model.predict(preprocessed_text)[0][0]  # Get the first output
    label = "Fake News" if prediction < 0.5 else "Real News"
    confidence = (1 - prediction) if prediction < 0.5 else prediction
    return label, confidence

# Streamlit UI for input and prediction
st.title("Fake News Detector")
input_text = st.text_area("Enter the text to check", height=200)

if st.button("Check"):
    if input_text.strip() != "":
        label, confidence = predict(input_text)
        st.write(f"Prediction: **{label}**")
        st.write(f"Confidence: **{confidence:.2f}**")
    else:
        st.write("Please enter some text.")

