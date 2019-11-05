import numpy as np
import cv2 as cv

img = np.full((512, 512, 3), 251.0)
cv.namedWindow('image')

def draw_circle(event, x, y, flags, params):
    ''' Callback function that draws a circle '''
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), 1)

cv.setMouseCallback('image', draw_circle)

while(True):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27: # esc key
        break

cv.destroyAllWindows()
