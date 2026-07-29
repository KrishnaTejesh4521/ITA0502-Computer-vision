import cv2

# Read the image
image = cv2.imread(r"E:\images.jpeg")

# Check if the image is loaded successfully
if image is None:
    print("Image not found!")
else:
    # Enlarge the image (2 times)
    bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Reduce the image (0.5 times)
    smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    # Wait until any key is pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
