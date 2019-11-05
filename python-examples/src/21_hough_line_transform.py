
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./images/sudoku.png")
img_2 = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150)

hough_pts_std = cv.HoughLines(edges, 1, np.pi/100, 200)

for line in hough_pts_std:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)


hough_pts_prob = cv.HoughLinesP(edges, 1, np.pi/100, 100, minLineLength=100, maxLineGap=10)

for line in hough_pts_prob:
    x1,y1,x2,y2 = line[0]
    cv.line(img_2,(x1,y1),(x2,y2),(0,255,0),2)


# plotting
plt.figure(num=None,figsize=(9,3), dpi=80, facecolor='w',edgecolor='k')

plt.subplot(1, 2, 1)
plt.xticks([]), plt.yticks([]), 
plt.title("HoughLines")
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.xticks([]), plt.yticks([]), 
plt.title("HoughLinesP")
plt.imshow(img_2)


# plt.show()
plt.savefig("ocv_hlt")

