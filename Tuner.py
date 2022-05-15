import numpy as np
import cv2
import Constants

class Tuner:

    def __int__(self, windowName):
        self.windowName = windowName
        self._mask = []

        cv2.createTrackbar(Constants.h_upper, windowName, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.s_upper, windowName, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.v_upper, windowName, 0, 255, self.__hsvTrackBarUpdate)

        cv2.createTrackbar(Constants.h_lower, windowName, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.s_lower, windowName, 0, 255, self.__hsvTrackBarUpdate)
        cv2.createTrackbar(Constants.v_lower, windowName, 0, 255, self.__hsvTrackBarUpdate)


    def __hsvTrackBarUpdate(self, hsv):

        color_upper = np.array([cv2.getTrackbarPos(Constants.h_upper, self.windowName),
                                cv2.getTrackbarPos(Constants.s_upper, self.windowName),
                                cv2.getTrackbarPos(Constants.v_upper, self.windowName)]
                               , np.uint8)
        color_lower = np.array([cv2.getTrackbarPos(Constants.h_lower, self.windowName),
                                cv2.getTrackbarPos(Constants.s_lower, self.windowName),
                                cv2.getTrackbarPos(Constants.v_lower, self.windowName)],
                               np.uint8)
        self.mask = cv2.inRange(hsv, color_lower, color_upper)


    def updateBinary(self):
        cv2.imshow(self.mask)