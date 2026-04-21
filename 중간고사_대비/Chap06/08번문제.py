import numpy as np, cv2

image1 = cv2.imread('images/add1.jpg')
image2 = cv2.imread('images/add2.jpg')

image3 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

concat = cv2.hconcat([image1, image3, image2])
cv2.imshow('image', concat)
cv2.waitKey(0)
cv2.destroyAllWindows()