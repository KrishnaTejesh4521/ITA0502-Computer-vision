import cv2

# Image path
image_path = r"E:\Computer vision Lab\Exp 3 Picture.jpg"

# Read the image
image = cv2.imread(image_path)

# Check if the image is loaded
if image is None:
    print("Error: Unable to load image. Check the file path.")
else:
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray_image, 100, 200)

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the outline (edges)
    cv2.imshow("Canny Edge Detection", edges)

    # Save the output image
    cv2.imwrite(r"E:\Computer vision Lab\Canny_Output.jpg", edges)

    print("Canny edge image saved successfully.")

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
