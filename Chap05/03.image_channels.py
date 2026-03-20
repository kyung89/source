import cv2

image = cv2.imread('images/color.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception('Could not open image')
if image.ndim != 3: raise Exception('Invalid image dimensions')

bgr = cv2.split(image)

print("bgr 자료형: ", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소 개수: ", len(bgr))

cv2.imshow('image', image)
cv2.imshow('Blue channel', bgr[0])
cv2.imshow('Green channel', bgr[1])
cv2.imshow('Red channel', bgr[2])

cv2.imshow('Blue channel2', image[:,:,0])
cv2.imshow('Green channel2', image[:,:,1])
cv2.imshow('Red channel2', image[:,:,2])

cv2.waitKey(0)