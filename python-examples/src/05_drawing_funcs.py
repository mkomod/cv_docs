import numpy as np
import cv2 as cv

img = np.full((512, 512, 3), 251.0)

# cv.line(img, (0, 0), (511, 511), (255, 0, 0), 2)
# cv.line(img, (511, 0), (0, 511), (0, 0, 255), 2)
# cv.imwrite("opencv_lines.png", img)

# cv.rectangle(img, (63, 63), (447, 447), (0, 255, 0), -1)

# cv.circle(img, (255, 255), 128, (0, 255, 100), 2)

cv.ellipse(img,(255, 255), (100, 200), 0, 90, 320, (0,0,255), -2)

# points = np.array([(63,63), (447, 127), (63, 195), (447, 255), (63, 319), (447, 383)], np.int32)
# points = points.reshape((-1, 1, 2))
# cv.polylines(img, [points], True, 255, 1)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "oCV", (200, 300), font, 2, (0, 0, 0), 2,cv.LINE_AA)


# cv.imwrite("opencv_text.png", img)
cv.imshow("img", img)
cv.waitKey(0)
cv.waitKey(0)
cv.destroyAllWindows()


