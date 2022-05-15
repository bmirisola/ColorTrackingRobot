import numpy as np
import cv2
from test import test_constants

def on_change(val=0):
    color_upper = np.array([cv2.getTrackbarPos(test_constants.h_upper,windowName),
                            cv2.getTrackbarPos(test_constants.s_upper,windowName),
                            cv2.getTrackbarPos(test_constants.v_upper,windowName)]
                           , np.uint8)
    color_lower = np.array([cv2.getTrackbarPos(test_constants.h_lower,windowName),
                            cv2.getTrackbarPos(test_constants.s_lower,windowName),
                            cv2.getTrackbarPos(test_constants.v_lower,windowName)],
                           np.uint8)
    mask = cv2.inRange(hsv,color_lower,color_upper)
    cv2.imshow('mask',mask)


img = cv2.imread('/home/bmirisola/PycharmProjects/ColorTrackingRobot/test/test.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
windowName = 'image'
cv2.namedWindow(windowName)

cv2.createTrackbar('h_upper', windowName, 0, 255, on_change)
cv2.createTrackbar('s_upper', windowName, 0, 255, on_change)
cv2.createTrackbar('v_upper', windowName, 0, 255, on_change)

cv2.createTrackbar('h_lower', windowName, 0, 255, on_change)
cv2.createTrackbar('s_lower', windowName, 0, 255, on_change)
cv2.createTrackbar('v_lower', windowName, 0, 255, on_change)

cv2.imshow(windowName, img)
on_change()
cv2.waitKey(0)
cv2.destroyAllWindows()
