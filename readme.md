# ParaDetect AI – Deep Learning Based Malaria Diagnosis

## Project Overview
ParaDetect AI is a deep learning-based system that detects malaria parasites in blood smear images. The user uploads a microscope image of blood cells, and the system predicts whether the image contains malaria parasites or not.

## Features
- Upload blood smear images
- Automatic malaria detection using AI
- Instant prediction results
- Simple web interface using Streamlit

## Technology Used
- Python
- TensorFlow (Deep Learning)
- OpenCV (Image Processing)
- NumPy
- Streamlit (Frontend Interface)

## How It Works
1. User uploads a blood cell image.
2. The image is processed using OpenCV.
3. A Convolutional Neural Network (CNN) analyzes the image.
4. The model predicts whether malaria parasites are present or not.

## Output
The system shows:
- Uploaded image
- Prediction result:
  - Parasitized (Malaria Detected)
  - Uninfected (No Malaria)

## How to Run the Project
Install required libraries:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Author
Hackathon Project – ParaDetect AI