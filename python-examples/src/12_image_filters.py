
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

lena = cv.imread("./images/lena.png")

# Mean Filtering
# lena_1 = cv.blur(lena, (10,10))
# lena_2 = cv.blur(lena, (30, 30))

# Median Filtering
# lena_1 = cv.medianBlur(lena, 9)
# lena_2 = cv.medianBlur(lena, 91)

# Gaussian Filtering
# lena_1 = cv.GaussianBlur(lena, (9, 9), 1)
# lena_2 = cv.GaussianBlur(lena, (31, 31), 5)

# Bilateral Filtering
lena_1 = cv.bilateralFilter(lena, 5, 75, 75)
lena_2 = cv.bilateralFilter(lena, 19, 400, 30)

lena_rgb = cv.cvtColor(lena, cv.COLOR_BGR2RGB)
lena_rgb_1 = cv.cvtColor(lena_1, cv.COLOR_BGR2RGB)
lena_rgb_2 = cv.cvtColor(lena_2, cv.COLOR_BGR2RGB)


plt.figure(num=None, figsize=(9, 3), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(131)
plt.imshow(lena_rgb)
plt.xticks([]), plt.yticks([]) 
plt.title("Lena")
plt.subplot(132)
plt.imshow(lena_rgb_1)
plt.xticks([]), plt.yticks([]) 
plt.title("d = 5,  $\sigma_{c} = 75,  \sigma_{s} = 75$")
plt.subplot(133)
plt.imshow(lena_rgb_2)
plt.xticks([]), plt.yticks([]) 
plt.title("d = 19,  $\sigma_{c} = 400,  \sigma_{s} = 30$")

# plt.savefig("ocv_bilateral_filtering")
plt.show()

