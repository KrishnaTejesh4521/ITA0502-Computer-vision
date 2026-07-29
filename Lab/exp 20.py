import cv2
import numpy as np

# Read the image
image = cv2.imread(r"E:\images.jpeg")

# Check if the image is loaded
if image is None:
    print("Image not found!")
else:
    # Define the Laplacian mask with negative center coefficient
    kernel = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]], dtype=np.float32)

    # Apply the Laplacian mask
    laplacian = cv2.filter2D(image, -1, kernel)

    # Sharpen the image
    sharpened = cv2.subtract(image, laplacian)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Laplacian Image", laplacian)
    cv2.imshow("Sharpened Image", sharpened)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
