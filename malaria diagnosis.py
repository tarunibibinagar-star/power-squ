import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

st.title("ParaDetect AI - Malaria Detection")

st.write("Upload a blood cell image to detect malaria.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    image = image.convert("RGB")
    
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = np.array(image)
    img = cv2.resize(img, (128,128))
    img = img.astype("float32") /255.0
    img = np.expand_dims(img, axis=0)

    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(128,128,3)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dense(1,activation='sigmoid')
    ])

    prediction = model.predict(img)

    if prediction > 0.5:
        st.success("Prediction: Parasitized (Malaria Detected)")
    else:
        st.success("Prediction: Uninfected (No Malaria)")