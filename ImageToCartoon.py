# import cv2
import cv2
import numpy as np
import streamlit as st
from PIL import Image

#
st.title("Web app to convert image to animated cartoon")

# Request for image upload
uploadImage = st.file_uploader("Please upload the image to convert to cartoon", type=["jpg","png"])

'Check if file is empty'
if uploadImage is None:
    st.text("Image missing! Please upload")
else:
    # Read image
    uploadedImage = Image.open(uploadImage)
    # uploadedImage = cv2.imread("C:\\Users\\agarakah\\Desktop\\26891940.jpg")
    st.image(uploadedImage, use_column_width=True)
    # Convert image to numpy array
    uploadedImage = np.asarray(uploadedImage)

    # Convert to grayscale
    grayScaledImage = cv2.cvtColor(uploadedImage, cv2.COLOR_BGR2GRAY)

    # Detect edges

    edgeDetectedImages = cv2.adaptiveThreshold(grayScaledImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)

    # Display images
    # cv2.imwrite("Cartoon.jpg",edgeDetectedImages)
    st.image(edgeDetectedImages, use_column_width=True)
print()
