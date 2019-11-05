import cv2 as cv
import numpy as np

img = np.full((512, 512, 3), 251.0)
cv.namedWindow('image')

def draw_circle(event, x, y, flags, params):
    ''' Callback function that draws a circle '''
    if event == cv.EVENT_LBUTTONDBLCLK:
        red = cv.getTrackbarPos("R", "image")
        thickness = cv.getTrackbarPos("T", "image")
        cv.circle(img, (x, y), 100, (0, 0, red), thickness)

def empty_func(x): pass

cv.createTrackbar("R", "image", 122, 255, empty_func)
cv.createTrackbar("T", "image", 5, 50, empty_func)
cv.setMouseCallback('image', draw_circle)

cv.createButton("some_name", empty_func, cv.QT_PUSH_BUTTON, 0)

while(True):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27: # esc key
        break

cv.destroyAllWindows()
