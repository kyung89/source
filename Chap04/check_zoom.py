import cv2

for backend_name, backend in [("DSHOW", cv2.CAP_DSHOW), ("MSMF", cv2.CAP_MSMF)]:
    cap = cv2.VideoCapture(0, backend)
    print(f"\nbackend={backend_name}, opened={cap.isOpened()}")
    if cap.isOpened():
        ok = cap.set(cv2.CAP_PROP_ZOOM, 4)
        cur = cap.get(cv2.CAP_PROP_ZOOM)
        print(" zoom -> ok:", ok, " current:", cur)

        ok = cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        cur = cap.get(cv2.CAP_PROP_AUTOFOCUS)
        print(" autofocus -> ok:", ok, " current:", cur)

        ok = cap.set(cv2.CAP_PROP_FOCUS, 10)
        cur = cap.get(cv2.CAP_PROP_FOCUS)
        print(" focus -> ok:", ok, " current:", cur)
    cap.release()