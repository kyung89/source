import numpy as np, cv2

def calc_histo(image, channels, bsize, ranges):
    shape = bsize if len(channels) >1 else (bsize[0], 1)
    hist = np.zeros(shape, np.int32)
    gap = np.divide(ranges[1::2], bsize)

    for row in image:
        for val in row:
            idx = np.divide(val[channels], gap).astype('uint')
            hist[tuple(idx)] += 1

    return hist

def calc_histo_original(image, hsize, ranges=[0, 256]):
    hist = np.zeros((hsize, 1), np.float32)
    gap = ranges[1]/hsize

    for i in (image/gap).flat:
        hist[int(i)] += 1
    return hist

image = cv2.imread("../images/pixel.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("Could not read the image")

# B, G, R 각각 8개 bin → 8 x 8 x 8 히스토그램
histSize = [8, 8, 8]
ranges = [0, 256, 0, 256, 0, 256]

hist1 = calc_histo(image, [0, 1, 2], histSize, ranges)

hist2 = cv2.calcHist(
    [image],
    [0, 1, 2],
    None,
    histSize,
    ranges
)

print("User 함수 shape:", hist1.shape)
print("OpenCV 함수 shape:", hist2.shape)

print("User 함수 flatten:\n", hist1.flatten())
print("OpenCV 함수 flatten:\n", hist2.flatten())