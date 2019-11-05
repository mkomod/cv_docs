
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("./images/noisy.png", 0)
img = cv.GaussianBlur(img, (5, 5), 0)

thresh, bin_img = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU) 

# bin_img = cv.morphologyEx(bin_img, cv.MORPH_CLOSE ,np.ones((9,9)))

plt.figure(num=None,figsize=(9,3), dpi=80, facecolor='w',edgecolor='k')

plt.subplot(131)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.xticks([]), plt.yticks([]) 

plt.subplot(132)
plt.hist(img.ravel(), bins=256)
plt.axvline(thresh, color='k', linewidth=1)
plt.text(thresh + 10, 2800, 't: %d' % thresh)
plt.title("Intensity")
plt.xticks([]), plt.yticks([]) 

plt.subplot(133)
plt.imshow(bin_img, cmap="gray")
plt.title("Otsu Binarization")
plt.xticks([]), plt.yticks([]) 

plt.show()
# plt.savefig("ocv_otsu")
