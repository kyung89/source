# 심화예저_7.4.4는 키보드로부터 영상파일의 번호를 입력받아서 열림 연산을 수행한다.
# 이 예제를 윗쪽과 아래쪽 화살표 키를 이용해서 다음 영상을 로드하여 수행하며, ESC 키를 누르면 종료하도록 수정하시오.

import numpy as np, cv2

no = 1

while True:
    # no = int(input("차량 영상 번호(0: 종료): "))
    # if no == 0: break

    key = cv2.waitKeyEx(0)
    if key == 2490368: # 윗쪽 화살표키 입력
        if no < 20: no += 1
        else:
            print("no = 20 을 초과하는 파일은 없습니다.")
            continue
    elif key == 2621440: # 아래쪽 화살표키 입력
        if no > 1: no -= 1
        else:
            print("no = 1 미만의 파일은 없습니다.")
            continue
    elif key == 27:
        print("ESC키를 입력했기에 종료합니다.")
        break

    print(no, "번 자동차 영상파일입니다.")
    fname = "../images/test_car/{0:02d}.jpg".format(no)
    image = cv2.imread(fname, cv2.IMREAD_COLOR)

    if image is None:
        print(str(no) + " 번 영상파일이 없습니다.")
        continue

    mask = np.ones((5, 17), np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (5, 5))
    gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5)

    ## 이진화 및 닫힘 연산 수행
    th_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)[1]
    morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=3)

    cv2.imshow("image", image)
    cv2.imshow("binary image", th_img)
    cv2.imshow("opening", morph)
    # cv2.waitKey(0)