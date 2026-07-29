import cv2
import numpy as np

# Image path
image_path = r"E:\Computer vision Lab\Exp 4 Picture.jpg"

# Read the image
image = cv2.imread(image_path)

# Check if the image is loaded
if image is None:
    print("Error: Unable to load image. Check the file path.")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Dilate the image
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the dilated image
    cv2.imshow("Dilated Image", dilated_image)

    # Save the dilated image
    cv2.imwrite(r"E:\Computer vision Lab\Dilated_Picture.jpg", dilated_image)

    print("Dilated image saved successfully.")

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
