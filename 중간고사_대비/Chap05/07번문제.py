import numpy as np, cv2

logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("ERROR")

blue, green, red = cv2.split(logo)

noimage = np.zeros(blue.shape, np.uint8)
blue_img = cv2.merge((blue, noimage, noimage))
green_img = cv2.merge((noimage, green, noimage))
red_img = cv2.merge((noimage, noimage, red))

cv2.imshow("logo", logo)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)
cv2.waitKey(0)