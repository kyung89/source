import cv2
import numpy as np
import glob
import os

def classify_weld(path):
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    if image is None:
        raise Exception("이미지 읽기 오류: " + path)

    h, w = image.shape[:2]
    result = image.copy()

    # 중앙 접합부 ROI
    x1 = int(w * 0.42)
    x2 = int(w * 0.58)
    y1 = int(h * 0.08)
    y2 = int(h * 0.82)

    roi = image[y1:y2, x1:x2]

    # 밝은 용접 비드 검출
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # 밝고 채도가 낮은 흰색/은색 용접부 검출
    mask = cv2.inRange(hsv, (0, 0, 185), (179, 95, 255))

    # 노이즈 제거 및 연결
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    label = "GOOD"
    color = (0, 255, 0)

    defect_area = 0
    defect_count = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area < 50:
            continue

        x, y, bw, bh = cv2.boundingRect(cnt)
        aspect = bw / bh if bh != 0 else 0

        touches_left = x <= 2

        # 불량 조건 1: 세로로 긴 용접 비드
        tall_defect = area > 2500 and bh > 140 and aspect < 0.8

        # 불량 조건 2: 둥글거나 넓게 튀어나온 하얀 용접 덩어리
        blob_defect = (
            area > 450 and
            bh > 20 and
            0.2 < aspect < 2.0 and
            not (touches_left and area < 12000)
        )

        if tall_defect or blob_defect:
            label = "BAD"
            color = (0, 0, 255)
            defect_count += 1
            defect_area = max(defect_area, area)

            cv2.rectangle(
                result,
                (x1 + x, y1 + y),
                (x1 + x + bw, y1 + y + bh),
                color,
                2
            )

    # ROI 표시
    cv2.rectangle(result, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.putText(
        result,
        label,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        color,
        3
    )

    print(os.path.basename(path), "=>", label,
          "defect_count:", defect_count,
          "max_defect_area:", defect_area)

    return image, mask, result


# 이미지가 현재 코드와 같은 폴더에 있는 경우
image_paths = sorted(glob.glob("*.jpg"))

# 과제4 폴더 안에 있는 경우는 아래 줄 사용
# image_paths = sorted(glob.glob("./과제4/*.jpg"))

for path in image_paths:
    original, mask, result = classify_weld(path)

    cv2.imshow("original", original)
    cv2.imshow("defect mask", mask)
    cv2.imshow("classification result", result)

    key = cv2.waitKey(0)
    if key == 27:
        break

cv2.destroyAllWindows()