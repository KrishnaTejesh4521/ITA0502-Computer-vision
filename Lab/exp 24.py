import cv2

# Read image
img = cv2.imread(r"E:\images.jpeg")

# Create blurred image
blur = cv2.GaussianBlur(img, (5, 5), 0)

# High-boost filtering
A = 2.0
high_boost = cv2.addWeighted(img, A, blur, -(A - 1), 0)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("High-Boost Sharpened Image", high_boost)

cv2.waitKey(0)
cv2.destroyAllWindows()
