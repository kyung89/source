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

while True:
    ret, frame = capture.read()
    if not ret: break

    zoom = capture.get(cv2.CAP_PROP_ZOOM)
    focus = capture.get(cv2.CAP_PROP_FOCUS)
    put_string(frame, "zoom: ", (10, 240), zoom)
    put_string(frame, "focus: ", (10, 270), focus)
    cv2.imshow(title, frame)

    if cv2.waitKey(30) >= 0: break
    if cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) < 1:
        break

capture.release()
cv2.destroyAllWindows()