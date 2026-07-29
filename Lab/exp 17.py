import cv2

# Read the image
image = cv2.imread(r"E:\images.jpeg")

# Check if the image is loaded
if image is None:
    print("Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel Edge Detection along X-axis
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

    # Convert the result to 8-bit image
    sobel_x = cv2.convertScaleAbs(sobel_x)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Sobel X Edge Detection", sobel_x)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
