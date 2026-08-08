import cv2
import numpy as np

# Read image
img = cv2.imread(r"E:\images.jpeg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convolution kernel for boundary detection
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Apply convolution
boundary = cv2.filter2D(gray, -1, kernel)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Image Boundary", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()
