
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread("./images/duck.webp")
img2 = img[:,:,::-1]

plt.subplot(121)
plt.subplot(121)
plt.title("BGR")
plt.imshow(img)
plt.subplot(122)
plt.title("RGB")
plt.imshow(img2)
plt.savefig("opencv_inv_cols")

# cv.imshow('', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

