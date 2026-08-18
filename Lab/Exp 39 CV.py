import cv2

# Video path
cap = cv2.VideoCapture(r"E:\Computer vision Lab\vidio.mp4")

# Vehicle cascade XML
car_cascade = cv2.CascadeClassifier(
    r"E:\Computer vision Lab\cars.xml"
)

# Check cascade
if car_cascade.empty():
    print("cars.xml could not be loaded")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30)
    )

    for x, y, w, h in cars:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Vehicle",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
