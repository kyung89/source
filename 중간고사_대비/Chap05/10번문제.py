# 10. PC 카메라로 영상을 읽어서 특정 부분(관심영역)의 합과 평균을 구하는 프로그램을 작성하시오.
# 1) 관심영역은 200, 100 좌표에서 200 x 100 크기로 한다.
# 2) cv2.mean() 함수를 사용하여 평균을 구하시오.
# 3) cv2.mean() 함수를 사용하지 않고 영상의 순회 방법으로 평균을 구하시오.

import numpy as np, cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception("ERROR")

frame_rate = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000 / frame_rate)

def user_mean(value):
    total = np.zeros(3)
    h, w = value.shape[:2]

    for i in range(h):
        for j in range(w):
            total += value[i, j]

    mean = total / (h * w)
    return (float(mean[0]), float(mean[1]), float(mean[2]), 0.0)

frame_cnt = 0
while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0: break
    frame_cnt += 1

    roi = frame[100:200, 200:400]
    cv2.rectangle(frame, (200, 100), (400, 200), (0, 0, 255), 1)

    if frame_cnt == 1:
        mean1 = cv2.mean(roi)
        print(mean1)
        mean2 = user_mean(roi)
        print(mean2)
    cv2.imshow("frame", frame)

capture.release()