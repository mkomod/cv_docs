
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

v = 255
main = []

for s in range(256):
    arr = []
    for h in np.arange(0, 180, 1):
        arr += [[h, s, v]]
    main += [arr]

img2 = np.uint8(main)
img3 = cv.cvtColor(img2, cv.COLOR_HSV2BGR)
img4 = cv.cvtColor(img3, cv.COLOR_BGR2RGB)

# plt.imshow(img4)
# plt.show()

# cv.imshow("img", img3)
# cv.waitKey(0)
# cv.destroyAllWindows()


