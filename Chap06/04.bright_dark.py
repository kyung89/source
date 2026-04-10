import cv2

image = cv2.imread("images/bright.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("No image")

dst1 = cv2.add(image, 100)
dst2 = cv2.subtract(image, 100)

dst3 = image + 100
dst4 = image - 100


cv2.imshow("original", image)
cv2.imshow("dst1: OpenCV", dst1)
cv2.imshow("dst2: OpenCV", dst2)
cv2.imshow("dst3: numpy", dst3)
cv2.imshow("dst4: numpy", dst4)
cv2.waitKey(0)