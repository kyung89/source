import numpy as np, cv2, math

idx = 0
pts1 = []
pts2 = []

def getLineLength(pt1, pt2):
    dx = np.float32(pt2[0] - pt1[0])
    dy = np.float32(pt2[1] - pt1[1])
    length = math.sqrt(dx*dx + dy*dy)
    return round(length, 2)

def getLineSlope(pt1, pt2):
    left, right = sort_points(pt1, pt2)
    dx = right[0] - left[0]
    dy = right[1] - left[1]
    if dx == 0: return None  # 수직선
    return round(- dy / dx, 2)
    # angle = cv2.fastAtan2(dy, dx)
    # return angle

def sort_points(pt1, pt2):

    if pt1[0] < pt2[0]:
        left = pt1
        right = pt2
    else:
        left = pt2
        right = pt1

    return left, right

def onMouse(event, x, y, flags, param):
    global image, idx
    if event == cv2.EVENT_LBUTTONDOWN:
        # print("마우스 눌렀다")
        pts1.append((x, y))

    if event == cv2.EVENT_LBUTTONUP:
        # print("마우스 뗐다")
        pts2.append((x, y))
        cv2.line(image, pts1[idx], pts2[idx], (0, 0, 255), 2)
        left, right = sort_points(pts1[idx], pts2[idx])
        cv2.putText(image, str(idx+1), right, 1, 1, (0, 0, 255), 1)
        cv2.imshow("image", image)

        # 직선의 길이와 기울기
        length = getLineLength(pts1[idx], pts2[idx])
        slope = getLineSlope(pts1[idx], pts2[idx])

        print()
        print("============")
        print((idx+1), " 번째 직선의 정보는 다음과 같습니다: ")
        print("직선의 길이: ", length)
        print("직선의 기울기: ", slope)
        print("============")
        print()

        idx = idx + 1

image = cv2.imread("../images/affine1.jpg", 1)
if image is None: raise Exception("영상파일 읽기 에러")

cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()