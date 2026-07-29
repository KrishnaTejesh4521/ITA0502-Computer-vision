import cv2

# Image path
image_path = r"E:\Computer vision Lab\exp 2 Picture1.jpg"

# Read the image
image = cv2.imread(image_path)

# Check if the image is loaded
if image is None:
    print("Error: Unable to load image. Check the file path.")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the blurred image
    cv2.imshow("Gaussian Blurred Image", blurred_image)

    # Save the blurred image
    cv2.imwrite(r"E:\Computer vision Lab\Blurred_Picture1.jpg", blurred_image)

    print("Gaussian Blurred image saved successfully.")

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
