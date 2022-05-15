import numpy as np
import cv2
import Constants


class Tuner:
    def __init__(self, window_name):
        self.windowName = window_name
        self._binaryImage = []
        self._hsvImage = []

        cv2.namedWindow(window_name)
        cv2.setMouseCallback(window_name, self.__print_bgr_of_hsv)
        cv2.createTrackbar(Constants.h_upper, window_name, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.s_upper, window_name, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.v_upper, window_name, 0, 255, self.__hsvTrackBarUpdate)

        cv2.createTrackbar(Constants.h_lower, window_name, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.s_lower, window_name, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.v_lower, window_name, 0, 255, self.__hsvTrackBarUpdate)

    def showBinary(self):
        cv2.imshow(self.windowName, self.mask)

    def setBinary(self, binary):
        self._binaryImage = binary

    def setHSV(self, hsv):
        self._hsvImage = hsv

    def __hsvTrackBarUpdate(self):
        color_upper = np.array([cv2.getTrackbarPos(Constants.h_upper, self.windowName),
                                cv2.getTrackbarPos(Constants.s_upper, self.windowName),
                                cv2.getTrackbarPos(Constants.v_upper, self.windowName)]
                               , np.uint8)
        color_lower = np.array([cv2.getTrackbarPos(Constants.h_lower, self.windowName),
                                cv2.getTrackbarPos(Constants.s_lower, self.windowName),
                                cv2.getTrackbarPos(Constants.v_lower, self.windowName)],
                               np.uint8)
        self.mask = cv2.inRange(self._hsvImage, color_lower, color_upper)

    def __print_bgr_of_hsv(self, event, x, y):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print(self._hsvImage[y][x])
