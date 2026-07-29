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

    # Source points (Original Image)
    src_points = np.array([
        [50, 50],
        [cols - 50, 50],
        [cols - 50, rows - 50],
        [50, rows - 50]
    ], dtype=np.float32)

    # Destination points (Transformed Image)
    dst_points = np.array([
        [20, 100],
        [cols - 100, 20],
        [cols - 20, rows - 100],
        [100, rows - 20]
    ], dtype=np.float32)

    # Compute Homography Matrix using Direct Linear Transformation (DLT)
    H, mask = cv2.findHomography(src_points, dst_points, method=0)

    # Apply the transformation
    transformed = cv2.warpPerspective(image, H, (cols, rows))

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("DLT Transformed Image", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
