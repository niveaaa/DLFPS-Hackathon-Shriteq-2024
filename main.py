import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import pickle
import streamlit as st

# Step 1: Load the Saved Model
model = tf.keras.models.load_model('image_model.h5')
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 2: Preprocessing Function for the Image
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize image
    image = img_to_array(image)  # Convert to numpy array
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image / 255.0  # Normalize pixel values
    return image

# Step 3: Prediction Function
def predict_image(image):
    image = preprocess_image(image)
    prediction = model.predict(image)[0][0]  # Extract prediction value
    label = "Real" if prediction < 0.5 else "AI Generated"
    confidence = round(abs(prediction - 0.5) * 2, 2)  # Confidence in [0, 1] range
    return label, confidence

# Step 4: Streamlit File Upload
st.title("Image Prediction App")
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    from PIL import Image
    image = Image.open(uploaded_file)
    label, confidence = predict_image(image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write(f"Prediction: {label}, Confidence: {confidence}")
