import cv2

# This has all the contours and classifies them into objects

class ContourFinder:

    def __init__(self, mask):
        self.mask = mask

        # Creating contour to track colored object
        contours, hierarchy = cv2.findContours(mask,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)