
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("./images/sudoku.png", 0)
img = cv.medianBlur(img, 5)

res_mean = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
res_gaus = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2) 


plt.figure(num=None,figsize=(9,3), dpi=80, facecolor='w',edgecolor='k')

plt.subplot(131)
plt.imshow(img, cmap="gray")
plt.xticks([]), plt.yticks([]) 
plt.title("Original")
plt.subplot(132)
plt.imshow(res_mean, cmap="gray")
plt.xticks([]), plt.yticks([]) 
plt.title("Mean Thresholding")
plt.subplot(133)
plt.imshow(res_gaus, cmap="gray")
plt.xticks([]), plt.yticks([]) 
plt.title("Gaussian Thresholding")


plt.show()
# plt.savefig("ocv_ith_adaptive.png")


