
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread("./images/lena.png", 0)

# resizing 
# res = cv.resize(img, None, fx=2, fy=2)
# height, width = img.shape[:2]
# res = cv.resize(img, (1*height, 2*width))

# rotation
# rows, cols = img.shape
# center = ((cols - 1)/2.0, (rows - 1)/2.0)
# M = cv.getRotationMatrix2D(center, 45, 1)
# res = cv.warpAffine(img, M, (cols, rows))
# title = "Rotation $ 45 \degree $ "


# translation 
# M =np.float32([
#     [1, 0, 0],
#     [0, 1, 0],
# ])
# res = cv.warpAffine(img, M, img.shape)
# title = "Translation by (100, 200) pixels"

# affine transformation

# rows, cols = img.shape
# pts1 = np.float32([ 
#     [20, 20],
#     [20, 100],
#     [100, 20]
# ])
# pts2 = np.float32([ 
#     [10, 50],
#     [25, 110],
#     [70, 60]
# ])
# M = cv.getAffineTransform(pts1, pts2)
# res = cv.warpAffine(img, M, (cols, rows))
# title = "Affine Transformation"

# perspective transformation

img = cv.imread("./images/sudoku.png")

pts1 = np.float32([[56,65], [368,52], [28,387], [389,390]])
pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])

M = cv.getPerspectiveTransform(pts1, pts2)
res = cv.warpPerspective(img,M,(300,300))
title = "Perspective Transformation"




plt.figure(num=None, figsize=(9,3), dpi=80, facecolor='w',edgecolor='k')

plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.xticks([]), plt.yticks([]) 
plt.title("Original")
plt.subplot(122)
plt.imshow(res)
plt.xticks([]), plt.yticks([]) 
plt.title(title)


plt.show()
# plt.savefig("ocv_gt_pertran.png")



