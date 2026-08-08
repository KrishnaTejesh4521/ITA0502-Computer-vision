import cv2
import numpy as np

# Read image
img = cv2.imread(r"E:\images.jpeg")

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(img, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
