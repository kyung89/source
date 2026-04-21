# 17. PC 카메라를 통해서 받아온 프레임을 좌우로 뒤집어서 "flip_test.avi" 이름의 동영상 파일로 저장하는 프로그램을 작성하시오.
# 1) 동영상 파일의 크기 640 x 480
# 2) 초당 프레임의 수: 15 fps
# 3) 동영상 코덱: DIVX

import numpy as np, cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception("ERROR")

frame_rate = 15
delay = int(1000 / frame_rate)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

writer = cv2.VideoWriter("flip_test.avi", fourcc, frame_rate, (640, 480))
if not writer.isOpened():
    raise Exception("ERROR: VideoWriter open failed")

while True:
    ret, frame = capture.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))  # 크기 맞추기
    image = cv2.flip(frame, 1)              # 좌우 뒤집기

    writer.write(image)

    cv2.imshow("frame", frame)
    if cv2.waitKey(delay) >= 0:
        break

writer.release()
capture.release()
cv2.destroyAllWindows()