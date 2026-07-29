import cv2

# Read the image
image = cv2.imread(r"E:\images.jpeg")

# Check if the image is loaded
if image is None:
    print("Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Canny Edge Detection", edges)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
