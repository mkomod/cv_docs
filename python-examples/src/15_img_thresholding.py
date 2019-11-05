
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# img_w = 180
# scale = 1.5
# img_h = round(256 * scale)

# img_arr = []

# for x in range(img_w):
#     col = []
#     for y in reversed(range(img_h)):
#        col += [[y / scale ]]
#     img_arr += [col]

# img = np.array(img_arr, np.uint8)

# cv.imwrite("range.png", img)

thresh = 160
img = cv.imread("./images/range.png")
arr, res1 = cv.threshold(img, thresh, 255, type=cv.THRESH_BINARY) 
arr, res2 = cv.threshold(img, thresh, 255, type=cv.THRESH_BINARY_INV) 
arr, res3 = cv.threshold(img, thresh, 255, type=cv.THRESH_TRUNC) 
arr, res4 = cv.threshold(img, thresh, 255, type=cv.THRESH_TOZERO) 
arr, res5 = cv.threshold(img, thresh, 255, type=cv.THRESH_TOZERO_INV) 

imgs = [(img, "Original"), (res1, "Binary"), (res2, "Binary Inv"), 
        (res3, "Truncated"), (res4, "To Zero"), (res5, "To Zero Inv")]

plt.figure(num=None,figsize=(9,4),dpi=80, facecolor='w',edgecolor='k')

for i, p in enumerate(imgs):
    plt.subplot(2, 3, 1+i)
    plt.imshow(p[0], cmap="gray")
    plt.xticks([]), plt.yticks([]) 
    plt.title(p[1])


# plt.show()
plt.savefig("ocv_ith_basic.png")


