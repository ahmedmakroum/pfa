import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
model_path = "/home/arx/Projects/pfa/sign_language_model.h5"  # Update this path if needed
try:
    model = load_model(model_path)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Define the mapping from class indices to letters
index_to_letter = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
    9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
    17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
}

# Streamlit app
st.title("Sign Language Recognition")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        # Preprocess the image
        img = image.load_img(uploaded_file, target_size=(64, 64))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Make a prediction
        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction)
        predicted_letter = index_to_letter[predicted_index]

        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.write(f"Predicted Letter: **{predicted_letter}**")
    except Exception as e:
        st.error(f"Error processing the image: {e}")