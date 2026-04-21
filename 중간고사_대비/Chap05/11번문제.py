import numpy as np, cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened():
    raise Exception("ERROR")

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = 30 if frame_rate == 0 else int(1000 / frame_rate)

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.resizeWindow("frame", 400, 300)

image = np.full((300, 400, 3), 0, np.uint8)

while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0:
        break

    frame = cv2.resize(frame, (320, 240))
    image[:] = 0

    image[30:270, 30:350] = frame
    cv2.rectangle(image, (30, 30), (350, 270), (0, 0, 255), 2)

    cv2.imshow("frame", image)

capture.release()
cv2.destroyAllWindows()