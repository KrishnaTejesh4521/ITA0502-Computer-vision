import cv2

# Read image
img = cv2.imread(r"E:\images.jpeg")

# Watermark text
text = "COMPUTER VISION"

# Position of watermark
position = (50, 50)

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2

# Add watermark
watermarked = img.copy()

cv2.putText(
    watermarked,
    text,
    position,
    font,
    font_scale,
    (255, 255, 255),
    thickness,
    cv2.LINE_AA
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", watermarked)

cv2.waitKey(0)
cv2.destroyAllWindows()
