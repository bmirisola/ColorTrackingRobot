# Python code for Multiple Color Detection


import numpy as np
import cv2

# Capturing video through webcam
webcam = cv2.VideoCapture(0)
webcam.set(3,640)
webcam.set(4,480)
webcam.set(cv2.CAP_PROP_EXPOSURE,-8)
webcam.set(cv2.CAP_PROP_AUTOFOCUS,0)

def print_bgr_of_hsv(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(hsvFrame[y][x])

cv2.namedWindow("original")
cv2.namedWindow("mask")
cv2.setMouseCallback("original", print_bgr_of_hsv)
cv2.setMouseCallback("mask", print_bgr_of_hsv)

# Start a while loop
while (1):

    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()

    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Set range for blue color and
    # define mask
    # B G R of HSV
    color_lower = np.array([107, 115, 78], np.uint8)
    color_upper = np.array([132, 240, 240], np.uint8)
    mask = cv2.inRange(hsvFrame, color_lower, color_upper)

    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    kernel = np.ones((5, 5), "uint8")

    # For blue color
    #mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Erosion then dilation
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(src=mask,kernel=kernel)
    #cv2.erode(mask,kernel)
    res_green = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

    # Creating contour to track green color
    contours, hierarchy = cv2.findContours(mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 500):
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h
            #print(aspect_ratio)
            # @TODO Better implement aspect ratio

            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 255, 0), 2)

            cv2.putText(imageFrame, "Frisbee", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))
            center = [x+w/2,y+h/2]
            print(center)



    # Program Termination
    cv2.imshow("Color Detector", imageFrame)
    cv2.imshow("mask",mask)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break
