import numpy as np, cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)

roi1 = image[10:110, 10:110]
roi2 = image[150:250, 150:250]

image[10:110, 10:110] = cv2.add(roi1, 50)
image[150:250, 150:250] = cv2.multiply(roi2, 1.8)

cv2.rectangle(image, (10, 10), (110, 110), (0, 0, 255), 2)
cv2.rectangle(image, (150, 150), (250, 250), (255, 0, 0), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()