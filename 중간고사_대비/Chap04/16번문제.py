# 16. PC 카메라를 통해서 받아온 프레임에 다음의 영상처리를 수행하고, 결과 영상을 윈도우에 표시하는 프로그램을 작성하시오.
# 1) (200, 100) 좌표에서 100 x 200 크기의 관심 영역 지정
# 2) 관심 영역에서 녹색 성분을 50만큼 증가
# 3) 관심 영역의 테두리를 두께 3의 빨간색으로 표시

import numpy as np, cv2

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not capture.isOpened(): raise Exception("ERROR")

frame_rate = 29.97
delay = int(1000 / frame_rate)

# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)


while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0: break

    roi = frame[100:300, 200:300]
    b, g, r = cv2.split(roi)
    cv2.add(g, 50, g)
    merged = cv2.merge((b,g,r))
    frame[100:300, 200:300] = merged
    cv2.rectangle(frame, (200, 100), (300, 300), (0, 0, 255), 3)

    cv2.imshow('frame',frame)

capture.release()
cv2.destroyAllWindows()