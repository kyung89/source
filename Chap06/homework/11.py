# cv2.calcHist() 함수는 1~3 채널 영상에 대해서 히스토그램을 계산할 수 있다.
# 예제_6.3.5 에서 calc_histo() 함수는 단일채널 영상에서  히스토그램을 계산하는데 cv2.calcHist() 함수와 같이 2채널 혹은 3채널 영상에서
# 2차원 혹은 3차원 히스토그램을 계산하도록 빈칸을 채우시오.

import numpy as np, cv2
# from Common.utils import ck_time

def calc_histo(image, channels, bsize, ranges):
    shape = bsize if len(channels) >1 else (bsize[0], 1)
    #hist = np.zeros((hsize, 1), np.float32)
    hist = np.zeros(shape, np.float32)
    # gap = np.divide(ranges[1::2], bins)
    gap = np.divide(np.array(ranges[1::2]) - np.array(ranges[::2]), bsize)

    # for i in (image/gap).flat:
    #     hist[int(i)] += 1

    for row in image:
        for val in row:
            idx = np.divide(val[channels], gap.astype('uint'))
            hist[tuple(idx)] += 1

    return hist

image = cv2.imread("pixel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Could not read the image")

histSize, ranges = [32], [0, 256]
gap = ranges[1]/histSize[0]
ranges_gap = np.arange(0, ranges[1]+1, gap)
hist1 = calc_histo(image, [0], histSize, ranges)
hist2 = cv2.calcHist([image], [0], None, histSize, ranges)
hist3, bins = np.histogram(image, ranges_gap)

print("User 함수: \n", hist1.flatten())
print("OpenCV 함수: \n", hist2.flatten())
print("numpy 함수: \n", hist3)