import cv2
import numpy as np
import glob
import os

def classify_product(path):
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    if image is None:
        raise Exception("이미지 읽기 오류: " + path)

    result = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (128, 128))

    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # 1. Laplacian 분산: 선명도 측정
    lap_var = cv2.Laplacian(blur, cv2.CV_64F).var()

    # 2. Canny 에지 개수
    edges = cv2.Canny(blur, 50, 120)
    edge_ratio = cv2.countNonZero(edges) / edges.size

    # 3. Sobel 평균 기울기
    gx = cv2.Sobel(blur, cv2.CV_32F, 1, 0, 3)
    gy = cv2.Sobel(blur, cv2.CV_32F, 0, 1, 3)
    mag = cv2.magnitude(gx, gy)
    sobel_mean = np.mean(mag)

    # 분류 기준
    # 정품: 경계가 뚜렷함 → lap_var, edge_ratio, sobel_mean 값이 큼
    if lap_var >= 6.0 and edge_ratio >= 0.02 and sobel_mean >= 25:
        label = "GOOD"
        color = (0, 255, 0)
    else:
        label = "BAD"
        color = (0, 0, 255)

    cv2.putText(result, label, (15, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.putText(result, f"lap={lap_var:.2f}", (15, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.putText(result, f"edge={edge_ratio:.3f}", (15, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    print(os.path.basename(path),
          "=>", label,
          "lap:", round(lap_var, 2),
          "edge:", round(edge_ratio, 3),
          "sobel:", round(sobel_mean, 2))

    return image, edges, result


# 같은 폴더의 jpg 전체 검사
image_paths = sorted(glob.glob("*.jpg"))

for path in image_paths:
    image, edges, result = classify_product(path)

    cv2.imshow("original", image)
    cv2.imshow("edges", edges)
    cv2.imshow("result", result)

    key = cv2.waitKey(0)
    if key == 27:
        break

cv2.destroyAllWindows()