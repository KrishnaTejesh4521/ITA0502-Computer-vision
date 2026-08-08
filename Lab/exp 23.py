import cv2

# Read image
img = cv2.imread(r"E:\images.jpeg")

# Create blurred image
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Unsharp masking
sharpened = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Unsharp Masked Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
