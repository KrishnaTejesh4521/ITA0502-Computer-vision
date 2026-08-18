import cv2

# Main image
img = cv2.imread(r"E:\images.jpeg")

# Watch template image
template = cv2.imread(r"E:\Computer vision Lab\images.jpg")

# Check images
if img is None:
    print("Main image not found")
    exit()

if template is None:
    print("Watch template not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Get template dimensions
h, w = template_gray.shape

# Template matching
result = cv2.matchTemplate(
    gray,
    template_gray,
    cv2.TM_CCOEFF_NORMED
)

# Find best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Detection threshold
threshold = 0.5

if max_val >= threshold:

    top_left = max_loc
    bottom_right = (
        top_left[0] + w,
        top_left[1] + h
    )

    # Draw rectangle around watch
    cv2.rectangle(
        img,
        top_left,
        bottom_right,
        (0, 255, 0),
        3
    )

    cv2.putText(
        img,
        "Watch Detected",
        (top_left[0], top_left[1] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    print("Watch Detected")
    print("Matching Score:", max_val)

else:
    print("Watch Not Detected")
    print("Matching Score:", max_val)

# Display result
cv2.imshow("Watch Recognition", img)
cv2.imshow("Watch Template", template)

cv2.waitKey(0)
cv2.destroyAllWindows()
