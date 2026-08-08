import cv2
import numpy as np

# Read image
img = cv2.imread(r"E:\images.jpeg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate gradients
gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Calculate gradient magnitude
gradient = cv2.magnitude(gx, gy)

# Convert gradient to 8-bit
gradient = cv2.convertScaleAbs(gradient)

# Create gradient mask
mask = cv2.cvtColor(gradient, cv2.COLOR_GRAY2BGR)

# Sharpen using gradient mask
sharpened = cv2.addWeighted(img, 1.0, mask, 1.0, 0)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Gradient Mask", mask)
cv2.imshow("Gradient Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
