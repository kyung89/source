# 13. 컬러 영상파일을 적재하여 "test.jpg" 와 "test.png" 파일로 각각 저장하시오. 이때 영상 파일을 가장 좋은 화질로 압축하시오.

import cv2

title = "13 PRACTICE"
image = cv2.imread("../images/read_color.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("image is None")

cv2.imwrite("test.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite("test.png", image, [cv2.IMWRITE_PNG_COMPRESSION, 0])

cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()