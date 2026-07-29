import cv2

# Read the image
image = cv2.imread(r"E:\images.jpeg")

# Check if the image is loaded
if image is None:
    print("Image not found!")
else:
    # Rotate the image 90 degrees clockwise
    clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Rotate the image 90 degrees counterclockwise
    counterclockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Clockwise Rotation", clockwise)
    cv2.imshow("Counter Clockwise Rotation", counterclockwise)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
