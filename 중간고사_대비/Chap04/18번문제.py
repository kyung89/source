import numpy, cv2
import numpy as np

image = np.zeros((300, 500, 3), np.uint8)
image[:] = 255

center = (image.shape[1] // 2, image.shape[0] // 2)

cv2.circle(image, center, 100, (0, 0, 255), -1)
cv2.ellipse(image, center, (100, 100), 0, 0, 180, (255, 0, 0), -1)
cv2.circle(image, (center[0] - 50, center[1]), 50, (0, 0, 255), -1)
cv2.circle(image, (center[0] + 50, center[1]), 50, (255, 0, 0), -1)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()