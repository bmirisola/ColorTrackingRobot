import time

import numpy as np
import cv2
import Constants

# Tuner should just look at existing mask and update it

class Tuner:
    def __init__(self, windowName, webcam):
        self.windowName = windowName
        self.webcam = webcam

        self._color_lower = np.array([107, 115, 78], np.uint8)
        self._color_upper = np.array([132, 240, 240], np.uint8)

        self._binaryImage = cv2.inRange(cv2.imread("test/test.jpg"), self._color_upper, self._color_upper)
        self._hsvImage = []

        cv2.namedWindow(windowName)
        cv2.setMouseCallback(windowName, self.__print_bgr_of_hsv)
        cv2.createTrackbar(Constants.h_upper, windowName, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.s_upper, windowName, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.v_upper, windowName, 0, 255, self.__hsvTrackBarUpdate)

        cv2.createTrackbar(Constants.h_lower, windowName, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.s_lower, windowName, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.v_lower, windowName, 0, 255, self.__hsvTrackBarUpdate)

    def showBinary(self):
        self._binaryImage = cv2.inRange(self._hsvImage, self._color_lower, self._color_upper)
        cv2.imshow(self.windowName, self._binaryImage)

    def setBinary(self, binary):
        self._binaryImage = binary

    def setHSV(self, hsv):
        self._hsvImage = hsv

    def __hsvTrackBarUpdate(self, val):
        self._color_upper = np.array([cv2.getTrackbarPos(Constants.h_upper, self.windowName),
                                cv2.getTrackbarPos(Constants.s_upper, self.windowName),
                                cv2.getTrackbarPos(Constants.v_upper, self.windowName)]
                               , np.uint8)
        self._color_lower = np.array([cv2.getTrackbarPos(Constants.h_lower, self.windowName),
                                cv2.getTrackbarPos(Constants.s_lower, self.windowName),
                                cv2.getTrackbarPos(Constants.v_lower, self.windowName)],
                               np.uint8)

    def __print_bgr_of_hsv(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print(self._hsvImage[y][x])
