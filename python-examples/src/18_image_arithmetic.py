import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


tools1 = cv.imread("./images/division1.png", 0)
tools2 = cv.imread("./images/division2.png", 0)

points = np.array([(127, 63), (63, 191), (191, 191)], np.int32)
points.reshape((-1, 1, 2))

triangle = cv.fillPoly(np.zeros((255, 255), np.uint8), [points], 170)
rectangle = cv.rectangle(np.zeros((255, 255), np.uint8), (63, 63), (191, 191), 80, -1)


circle = cv.circle(np.zeros((255, 255), np.uint8), (127, 127), 64, 255, -1)
circle_r = cv.circle(np.zeros((255, 255), np.uint8), (159, 127), 64, 255, -1)
circle_l = cv.circle(np.zeros((255, 255), np.uint8), (93, 127), 64, 255, -1)


imgs = [("A", rectangle), ("B", triangle),]

# addition
# imgs += [("A+B", rectangle + triangle), 
#          ("A+100", rectangle + 100)]


# subtraction
# rectangle = cv.rectangle(np.zeros((255, 255), np.uint8), (63, 63), (191, 191), 200, -1)
# triangle = cv.fillPoly(np.zeros((255, 255), np.uint8), [points], 200)
# imgs = [("A", rectangle), ("B", triangle),]
# imgs += [("A-B", rectangle - triangle), 
#          ("A-200", rectangle - 200)]


# multiplication 
# mult = cv.imread("./images/multiplication.png", 0)
# imgs = [("A", mult)]
# imgs += [("$A \\times 0.5 $", mult * 0.5),
#          ("$A \\times 2.0 $", mult * 5.0)]


# division
# imgs = [("A", tools1), ("B", tools2)]
# imgs += [("$(A \div B) \\times 100 $", (tools1 / tools2) * 100)]


# AND / OR / XOR
# res = np.logical_and(circle_r, circle_l)
# res = np.logical_or(circle_r, circle_l)
# res = np.logical_xor(circle_r, circle_l)
# imgs = [("A", circle_l), ("B", circle_r)]
# imgs += [("$ A \\veebar B $", res)]

# NOT
res = np.logical_not(circle)
imgs = [("A", circle)]
imgs += [("$ \\neg A $", res)]


plt.figure(num=None,figsize=(9,3), dpi=80, facecolor='w',edgecolor='k')

for i, img in enumerate(imgs):
    plt.subplot(1,len(imgs), 1+i)
    plt.xticks([]), plt.yticks([]), 
    plt.title(img[0])
    plt.imshow(img[1], cmap="gray")

plt.show()
# plt.savefig("ocv_NOT")





