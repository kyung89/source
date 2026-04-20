# 15. 심화예제_4.5.2인 18.set_camera_attr.py를 수정해서 트랙바로 카메라 영상의 밝기와 대비 변경할 수 있도록 수정하시오.

import cv2
from Common.utils import put_string

def zoom_bar(value):
    global capture
    ok = capture.set(cv2.CAP_PROP_ZOOM, value)
    current = capture.get(cv2.CAP_PROP_ZOOM)
    print(f"zoom set: {value}, ok={ok}, current={current}")

def focus_bar(value):
    global capture
    ok = capture.set(cv2.CAP_PROP_FOCUS, value)
    current = capture.get(cv2.CAP_PROP_FOCUS)
    print(f"focus set: {value}, ok={ok}, current={current}")

def brightness_bar(value):
    global capture
    ok = capture.set(cv2.CAP_PROP_BRIGHTNESS, value)
    current = capture.get(cv2.CAP_PROP_BRIGHTNESS)
    print(f"brightness set: {value}, ok={ok}, current={current}")

def contrast_bar(value):
    global capture
    ok = capture.set(cv2.CAP_PROP_CONTRAST, value)
    current = capture.get(cv2.CAP_PROP_CONTRAST)
    print(f"contrast set: {value}, ok={ok}, current={current}")

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not capture.isOpened(): raise Exception("Could not open camera")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

af_ok = capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
print("autofocus off:", af_ok, "current:", capture.get(cv2.CAP_PROP_AUTOFOCUS))

capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)

title = "Change Camera Properties"
cv2.namedWindow(title)
cv2.createTrackbar("zoom", title, 0, 10, zoom_bar)
cv2.createTrackbar("focus", title, 0, 40, focus_bar)

cv2.createTrackbar("Brightness", title, 0, 100, brightness_bar)
cv2.createTrackbar("Contrast", title, 0, 100, contrast_bar)

while True:
    ret, frame = capture.read()
    if not ret: break

    zoom = capture.get(cv2.CAP_PROP_ZOOM)
    focus = capture.get(cv2.CAP_PROP_FOCUS)
    brightness = capture.get(cv2.CAP_PROP_BRIGHTNESS)
    contrast = capture.get(cv2.CAP_PROP_CONTRAST)
    put_string(frame, "zoom: ", (10, 240), zoom)
    put_string(frame, "focus: ", (10, 270), focus)
    put_string(frame, "brightness: ", (10, 300), brightness)
    put_string(frame, "contrast: ", (10, 330), contrast)
    cv2.imshow(title, frame)

    if cv2.waitKey(30) >= 0: break
    if cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) < 1:
        break

capture.release()
cv2.destroyAllWindows()