
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("./images/sudoku.png", 0)
imgs = [("Original", img)]

# sobel
# res_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
# res_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
# imgs += [("Sobel X", res_x), ("Sobel Y", res_y)]

# scharr
# res_sch = cv.Scharr(img, cv.CV_64F, 1, 0)
# imgs += [("Sobel G_x", res_sch)]

# laplacian
res_lap = cv.Laplacian(img, cv.CV_64F)
imgs += [("Laplacian", res_lap)]

# plotting
plt.figure(num=None,figsize=(9,3), dpi=80, facecolor='w',edgecolor='k')

# for i, img in enumerate(imgs):
#     plt.subplot(1,len(imgs), 1+i)
#     plt.xticks([]), plt.yticks([]), 
#     plt.title(img[0])
#     plt.imshow(img[1], cmap="gray") 

plt.subplot(1, 2, 1)
plt.xticks([]), plt.yticks([]), 
plt.title("Original")
plt.imshow(img, cmap="gray") 

plt.subplot(1, 2, 2)
plt.xticks([]), plt.yticks([]), 
plt.title("Laplacian")
plt.imshow(res_lap, cmap="gray", vmin=0, vmax=20)

plt.show()
# plt.savefig("ocv_laplace")

