import cv2
import numpy as np
# import streamlit as st
#
# st.title("Stream")

# Read image
uploadedImage = cv2.imread("C:\\Users\\agarakah\\Desktop\\26891940.jpg")

# Convert to grayscale
grayScaledImage = cv2.cvtColor(uploadedImage, cv2.COLOR_BGR2GRAY)

# Detect edges

edgeDetectedImages = cv2.adaptiveThreshold(grayScaledImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)

# Display images
cv2.imwrite("Cartoon.jpg",edgeDetectedImages)
print()
