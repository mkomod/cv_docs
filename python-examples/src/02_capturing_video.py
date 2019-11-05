import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    res, frame = cap.read() # combines cap.grab() and cap.retrieve()

    if not res:
        print("Can't receive frame")
        break

    # gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', frame) # display

    if cv.waitKey(1) == ord('q'):
        break

cap.release() # close capture stream
cv.destroyAllWindows()
