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

    # Four points from the original image
    pts1 = np.float32([[50, 50],
                       [300, 50],
                       [50, 300],
                       [300, 300]])

    # Corresponding points in the output image
    pts2 = np.float32([[10, 100],
                       [280, 50],
                       [80, 280],
                       [320, 300]])

    # Compute perspective transformation matrix
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply perspective transformation
    perspective = cv2.warpPerspective(image, M, (cols, rows))

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformed Image", perspective)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
