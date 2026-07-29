import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

# Check if webcam is opened
if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    print("Press 's' for Slow Motion")
    print("Press 'f' for Fast Motion")
    print("Press 'n' for Normal Speed")
    print("Press 'q' to Quit")

    delay = 30  # Normal speed

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame.")
            break

        # Display webcam video
        cv2.imshow("Webcam Video", frame)

        key = cv2.waitKey(delay) & 0xFF

        if key == ord('s'):
            delay = 100    # Slow Motion
        elif key == ord('f'):
            delay = 5      # Fast Motion
        elif key == ord('n'):
            delay = 30     # Normal Speed
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
