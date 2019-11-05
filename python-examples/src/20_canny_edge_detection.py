
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./images/grasshopper.png", 0)
imgs = [("Original", img)]

canny = cv.Canny(img, 80, 180)


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
plt.title("Canny")
plt.imshow(canny, cmap="gray")

# plt.show()
plt.savefig("ocv_canny")

