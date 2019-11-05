import numpy as np
import cv2 as cv


cap = cv.VideoCapture("./videos/video.mp4")

while True:
    res, frame = cap.read() # combines cap.grab() and cap.retrieve()

    if not res:
        print("Can't receive frame")
        break

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray_frame) # display

    if cv.waitKey(1) == ord('q'):
        break

cap.release() # close capture stream
cv.destroyAllWindows()
