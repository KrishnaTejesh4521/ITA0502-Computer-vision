import cv2
import numpy as np

# Read the video
cap = cv2.VideoCapture(r"E:\Computer vision Lab\vidio.mp4")

# Check if the video is opened successfully
if not cap.isOpened():
    print("Error: Cannot open video!")
else:
    while True:
        # Read a frame
        ret, frame = cap.read()

        if not ret:
            break

        # Get frame dimensions
        rows, cols = frame.shape[:2]

        # Define four points in the original frame
        pts1 = np.float32([
            [50, 50],
            [cols - 50, 50],
            [50, rows - 50],
            [cols - 50, rows - 50]
        ])

        # Define corresponding points in the transformed frame
        pts2 = np.float32([
            [0, 100],
            [cols, 0],
            [100, rows],
            [cols - 100, rows - 50]
        ])

        # Compute the perspective transformation matrix
        M = cv2.getPerspectiveTransform(pts1, pts2)

        # Apply perspective transformation
        transformed = cv2.warpPerspective(frame, M, (cols, rows))

        # Display the original and transformed frames
        cv2.imshow("Original Video", frame)
        cv2.imshow("Perspective Transformed Video", transformed)

        # Press 'q' to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Release the video object and close windows
cap.release()
cv2.destroyAllWindows()
