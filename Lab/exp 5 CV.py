import cv2
import numpy as np

# Image path
image_path = r"E:\Computer vision Lab\Exp 5 Picture.jpg"

# Read the image
image = cv2.imread(image_path)

# Check if the image is loaded
if image is None:
    print("Error: Unable to load image. Check the file path.")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Erode the image
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the eroded image
    cv2.imshow("Eroded Image", eroded_image)

    # Save the eroded image
    cv2.imwrite(r"E:\Computer vision Lab\Eroded_Picture.jpg", eroded_image)

    print("Eroded image saved successfully.")

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
