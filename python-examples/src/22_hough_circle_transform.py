
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# load image
img = cv.imread("./images/coins_2.png")

# process image
img = cv.medianBlur(img, 7)
img_gr = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_edg = cv.Canny(img_gr, 100, 220)

# apply hough circle transform
circles = cv.HoughCircles(img_gr, cv.HOUGH_GRADIENT, 1, 
        minDist=60, param1=150, param2=60, 
        minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))

for cir in circles[0,:]:
    center = (cir[0], cir[1])
    rad = cir[2]
    # draw the outer circle
    cv.circle(img, center, rad, (0,255,0), 20)
    # draw marker at center
    cv.circle(img, center, 20, (0,0,255), -1)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB) 
imgs = [
        ("Original", img_gr),
        ("Edges", img_edg),
        ("Hough Circles", img)
]

# plotting
plt.figure(num=None,figsize=(9,3), dpi=80, facecolor='w',edgecolor='k')

for i, img in enumerate(imgs):
    plt.subplot(1,len(imgs), 1+i)
    plt.xticks([]), plt.yticks([]), 
    plt.title(img[0])
    plt.imshow(img[1], cmap="gray") 

plt.show()
# plt.savefig("ocv_hough_circ")


