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
    src_points = np.float32([
        [50, 50],
        [cols - 50, 50],
        [50, rows - 50],
        [cols - 50, rows - 50]
    ])

    # Corresponding points in the transformed image
    dst_points = np.float32([
        [0, 100],
        [cols - 100, 0],
        [100, rows - 50],
        [cols, rows]
    ])

    # Find the Homography matrix
    H, status = cv2.findHomography(src_points, dst_points)

    # Apply the Homography transformation
    transformed = cv2.warpPerspective(image, H, (cols, rows))

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Homography Transformed Image", transformed)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
