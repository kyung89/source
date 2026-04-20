# 14. 심화예제_4.3.5인 11.event_draw.py를 수정해서 마우스 중간버튼을 클릭하여 타원을 그리세요.

import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0: pt = (x, y)
        else:
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0: pt = (x, y)
        else:
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx*dx + dy*dy))
            cv2.circle(image, pt, radius, (0, 0, 255), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)

    elif event == cv2.EVENT_MBUTTONDOWN:
        if pt[0] < 0: pt = (x, y)
        else:
            # dx, dy = abs(pt[0] - x), abs(pt[1] - y)
            # cv2.ellipse(image, pt, (dx, dy), 0, 0, 360, (0, 0, 0), 1)
            center = ((pt[0] + x) // 2, (pt[1] + y) // 2)
            axes = (abs(pt[0] - x) // 2, abs(pt[1] - y) // 2)
            cv2.ellipse(image, center, axes, 0, 0, 360, (0, 0, 0), 1)
            cv2.imshow(title, image)
            pt = (-1, -1)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)