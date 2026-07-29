import cv2

# Video path
video_path = r"E:\Computer vision Lab\Exp 6 vidio.mp4"

# Open the video
cap = cv2.VideoCapture(video_path)

# Check if the video is opened successfully
if not cap.isOpened():
    print("Error: Unable to open the video. Check the file path.")
else:
    print("Press 's' for Slow Motion")
    print("Press 'f' for Fast Motion")
    print("Press 'n' for Normal Speed")
    print("Press 'q' to Quit")

    delay = 30  # Normal speed

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Display the video
        cv2.imshow("Video Player", frame)

        key = cv2.waitKey(delay) & 0xFF

        if key == ord('s'):
            delay = 100   # Slow Motion
        elif key == ord('f'):
            delay = 5     # Fast Motion
        elif key == ord('n'):
            delay = 30    # Normal Speed
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
