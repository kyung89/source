# 18. 다음과 같이 태극 문양을 그리는 프로그램을 작성하시오.
# 힌트:
# 1) 태극은 반원이 4개 필요하다.
# 2) 반원은 타원 그리기 함수로 그릴 수 있다.
# 3) 영상의 너비와 높이는 3대 2비율이며, 태극의 반지름은 높이의 1/4이다.

import numpy as np, cv2

title = "image"
width, height = 600, 400
image = np.zeros((height,width,3), dtype = "uint8")
image[:] = 255

red, blue = (0, 0, 255), (255, 0, 0)
center = (width//2, height//2)
sub_center1 = (width//2 - 50, height//2)
sub_center2 = (width//2 + 50, height//2)
cv2.ellipse(image, center, (100, 100), 0, 180, 360, red, -1)
cv2.ellipse(image, center, (100, 100), 0, 0, 180, blue, -1)
cv2.ellipse(image, sub_center1, (50, 50), 0, 0, 180, red, -1)
cv2.ellipse(image, sub_center2, (50, 50), 0, 180, 360, blue, -1)

cv2.namedWindow(title)
cv2.imshow(title,image)

cv2.waitKey(0)
cv2.destroyAllWindows()