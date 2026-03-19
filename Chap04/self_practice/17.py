# 17. PC 카메라를 통해서 받아온 프레임을 좌우로 뒤집어서 "flip_test.avi" 이름의 동영상 파일로 저장하는 프로그램을 작성하시오.
# 1) 동영상 파일의 크기 640x480
# 2) 초당 프레임 수: 15 fps
# 3) 동영상 코덱: DIVX

import numpy as np, cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception("Could not open webcam")

fps = 15
delay = round(1000/fps)

ret, frame = capture.read()
if not ret:
    raise Exception("첫 프레임 읽기 실패")

h, w = frame.shape[:2]
size = (w, h)

print("actual size:", size)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter('flip_test.avi', fourcc, fps, size)
if not writer.isOpened(): raise Exception("동영상 파일 개방 안됨")

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    flipped = cv2.flip(frame, 1)  # 🔥 좌우 반전

    cv2.imshow("Original", frame)
    cv2.imshow("Flipped", flipped)
    writer.write(flipped)

    if cv2.waitKey(delay) >= 0:
        break

writer.release()
capture.release()
cv2.destroyAllWindows()