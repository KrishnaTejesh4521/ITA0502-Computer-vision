import cv2

img = cv2.imread(r"E:\images.jpeg")

x = 100
y = 100
w = 200
h = 200

cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

object_img = img[y:y+h, x:x+w]

cv2.imshow("Original with Rectangle", img)
cv2.imshow("Extracted Object", object_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
