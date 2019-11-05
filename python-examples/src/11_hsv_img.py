
import cv2 as cv


duck = cv.imread("./images/duck.webp")
hsv_duck = cv.cvtColor(duck, cv.COLOR_BGR2HSV)

cv.imwrite("ocv_hsv_duck.png", duck)

