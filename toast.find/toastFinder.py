import numpy as np
import cv2
import time

MINIMUM_AREA_FOR_TOAST = 100000 # may need to adjust this for differnet cameras

def find_toast(image: str):
    # print(type(image))
    # image = cv2.imread(image)
    hh, ww = image.shape[:2]
    image = image - 15
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

    lower = np.array([20, 0, 0])
    upper = np.array([100, 255, 255])
    imgRange = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("green part of image", imgRange)

    imgForeground = cv2.bitwise_not(imgRange)
    cv2.imshow("foreground", imgForeground)

    #kernels for morphology operations
    kernel_noise = np.ones((6,6),np.uint8) #to delete small noises
    kernel_dilate = np.ones((30,30),np.uint8)  #bigger kernel to fill holes after ropes
    kernel_erode = np.ones((38,38),np.uint8)  #bigger kernel to delete pixels on edge that was add after dilate function

    imgErode = cv2.erode(imgForeground, kernel_noise, 1)
    imgDilate = cv2.dilate(imgErode , kernel_dilate, 1)
    imgErode = cv2.erode(imgDilate, kernel_erode, 1)
    cv2.imshow("cleaned foreground", imgErode)

    contours, _ = cv2.findContours(imgErode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return

    # Find the largest contour by area
    largest_contour = max(contours, key=cv2.contourArea)

    print(cv2.contourArea(largest_contour))
    if (cv2.contourArea(largest_contour) < MINIMUM_AREA_FOR_TOAST):
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return -1, -1

    # Create a mask for the largest region
    mask = np.zeros_like(imgErode)
    cv2.drawContours(mask, [largest_contour], -1, (255), thickness=cv2.FILLED)

    M = cv2.moments(largest_contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(mask, (cX, cY), 70, (0, 0, 0), -1) # draw circle in middle of toats

    # Show result
    cv2.imshow("Largest Region", mask)

    cv2.imwrite("OUTPUT.png", mask)

    return cX, cY, time.time()
