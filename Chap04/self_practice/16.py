# 16. PC 카메라를 통해서 받아온 프레임에 다음의 영상처리를 수행하고, 결과 영상을 윈도우에 표시하는 프로그램을 작성하시오.
# 1) (200, 100) 좌표에서 100x200 크기의 관심 영역 지정
# 2) 관심 영역에서 녹색 성분을 50만큼 증가
# 3) 관심 영역의 테두리를 두께 3의 빨간색으로 표시

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

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    roi = frame[100:300, 200:300]

    # 2) ROI의 녹색 성분 50 증가
    roi[:, :, 1] = np.clip(roi[:, :, 1].astype(np.int16) + 50, 0, 255).astype(np.uint8)

    # 3) ROI 테두리를 두께 3의 빨간색으로 표시
    cv2.rectangle(frame, (200, 100), (300, 300), (0, 0, 255), 3)

    cv2.imshow("Result", frame)

    if cv2.waitKey(delay) >= 0:
        break

capture.release()
cv2.destroyAllWindows()