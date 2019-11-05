
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./images/coins.png")

# Erosion
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img, kernel, iterations=1)

# Dilation
kernel = np.ones((3,3),np.uint8)
dilation = cv.dilate(img, kernel, iterations=1)
# dilation = dilation - img

# Morph Grad
grad = cv.morphologyEx(img, cv.MORPH_GRADIENT, cv.getStructuringElement(cv.MORPH_RECT, (3, 3)))

plt.figure(num=None, figsize=(9, 3), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.title("Original")
plt.subplot(122)
# plt.imshow(erosion)
# plt.imshow(dilation)
plt.imshow(grad)
plt.title("Morphological Gradient")
plt.xticks([]), plt.yticks([])



# plt.show()
plt.savefig("ocv_grad.png")





