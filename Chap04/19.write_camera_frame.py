import cv2

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not capture.isOpened(): raise Exception("Could not open camera")

fps = 29.97
delay = round(1000/fps)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

ret, frame = capture.read()
if not ret:
    raise Exception("첫 프레임 읽기 실패")

h, w = frame.shape[:2]
size = (w, h)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

print("width x height: ", size)
print("VideoWriterfourcc: %s" % fourcc)
print("delay: %2d ms" % delay)
print("fps: %.2f" % fps)

capture.set(cv2.CAP_PROP_ZOOM, 1)
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

writer = cv2.VideoWriter('images/video_file.avi', fourcc, fps, size)
if not writer.isOpened(): raise Exception("동영상 파일 개방 안됨")

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(delay) >= 0: break

    cv2.imshow('View Frame from Camera', frame)
    writer.write(frame)

    if cv2.waitKey(delay) >= 0:
        break

writer.release()
capture.release()
cv2.destroyAllWindows()