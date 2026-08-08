import cv2

# Read image
img = cv2.imread(r"E:\images.jpeg")

# Crop a portion of the image
crop = img[50:150, 50:150]

# Copy the original image
result = img.copy()

# Get image dimensions
h, w = result.shape[:2]

# Position where cropped image will be pasted
x = 20
y = 20

# Get crop dimensions
ch, cw = crop.shape[:2]

# Paste cropped image
result[y:y+ch, x:x+cw] = crop

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Cropped and Pasted Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
