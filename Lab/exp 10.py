import cv2
import numpy as np

# Read the image
image = cv2.imread(r"E:\images.jpeg")

# Check if the image is loaded
if image is None:
    print("Image not found!")
else:
    # Get image dimensions
    rows, cols = image.shape[:2]

    # Translation matrix
    # Move the image 100 pixels to the right and 50 pixels down
    M = np.float32([[1, 0, 100],
                    [0, 1, 50]])

    # Apply translation
    moved = cv2.warpAffine(image, M, (cols, rows))

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Moved Image", moved)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
