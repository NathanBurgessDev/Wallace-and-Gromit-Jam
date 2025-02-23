import numpy as np
import cv2
import time

MINIMUM_AREA_FOR_TOAST = 60000 # may need to adjust this for differnet cameras
# MINIMUM_AREA_FOR_TOAST = 200000

def find_toast(image: str):

    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(imgHSV)
    v = np.clip(v * 0.50, 0, 255).astype(np.uint8)  # Reduce brightness by 50%

    # Merge back
    hsv_modified = cv2.merge([h, s, v])
    # cv2.imshow('darkened', hsv_modified)

    lower = np.array([20, 0, 0])
    upper = np.array([100, 255, 255])
    imgRange = cv2.inRange(hsv_modified, lower, upper)
    # cv2.imshow("green part of image", imgRange)

    imgForeground = cv2.bitwise_not(imgRange)
    cv2.imshow("foreground", imgForeground)

    #kernels for morphology operations
    kernel_noise = np.ones((6,6),np.uint8) #to delete small noises
    kernel_dilate = np.ones((30,30),np.uint8)  #bigger kernel to fill holes after ropes
    kernel_erode = np.ones((38,38),np.uint8)  #bigger kernel to delete pixels on edge that was add after dilate function

    imgErode = cv2.erode(imgForeground, kernel_noise, 1)
    imgDilate = cv2.dilate(imgErode , kernel_dilate, 1)
    imgErode = cv2.erode(imgDilate, kernel_erode, 1)
    # cv2.imshow("cleaned foreground", imgErode)

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

    # if M["m00"] == 0:
    #     return

    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(mask, (cX, cY), 70, (0, 0, 0), -1) # draw circle in middle of toats

    # Show result
    cv2.imshow("Largest Region", mask)

    return cX, cY, time.time(), mask, image

# def toastFinderBrownness(image):
#     image = image - 15
#     imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#     # lower boundary RED color range values; Hue (0 - 10)
#     lower1 = np.array([0, 100, 20])
#     upper1 = np.array([10, 255, 255])
    
#     # upper boundary RED color range values; Hue (160 - 180)
#     lower2 = np.array([160,100,20])
#     upper2 = np.array([179,255,255])
    
#     lower_mask = cv2.inRange(image, lower1, upper1)
#     cv2.imshow("darker red", lower_mask)
#     upper_mask = cv2.inRange(image, lower2, upper2)
#     cv2.imshow("brighter red", upper_mask)
   
#     full_mask = lower_mask + upper_mask
#     result = image.copy()
#     result = cv2.bitwise_and(result, result, mask=full_mask)
#     cv2.imshow('mask', full_mask)
#     cv2.imshow('result', result)

#     #kernels for morphology operations
#     kernel_noise = np.ones((6,6),np.uint8) #to delete small noises
#     kernel_dilate = np.ones((30,30),np.uint8)  #bigger kernel to fill holes after ropes
#     kernel_erode = np.ones((38,38),np.uint8)  #bigger kernel to delete pixels on edge that was add after dilate function

#     imgErode = cv2.erode(full_mask, kernel_noise, 1)
#     imgDilate = cv2.dilate(imgErode , kernel_dilate, 1)
#     imgErode = cv2.erode(imgDilate, kernel_erode, 1)
#     cv2.imshow("cleaned foreground", imgErode)

#     contours, _ = cv2.findContours(imgErode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     if len(contours) == 0:
#         return

#     largest_contour = max(contours, key=cv2.contourArea)

#     mask = np.zeros_like(imgErode)
#     cv2.drawContours(mask, [largest_contour], -1, (255), thickness=cv2.FILLED)

#     M = cv2.moments(largest_contour)

#     if M["m00"] == 0:
#         return

#     cX = int(M["m10"] / M["m00"])
#     cY = int(M["m01"] / M["m00"])
#     cv2.circle(mask, (cX, cY), 70, (0, 0, 0), -1) # draw circle in middle of toats
#     cv2.imwrite("OUTPUT.png", mask)

#     return cX, cY, time.time()



# def toastFinderBrownness(image):
#     image = image - 15
#     imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#     # lower boundary RED color range values; Hue (0 - 10)
#     lower1 = np.array([10, 100, 20])
#     upper1 = np.array([20, 255, 200])

#     lower_mask = cv2.inRange(imgHSV, lower1, upper1)
#     cv2.imshow("brown", lower_mask)

#     #kernels for morphology operations
#     # kernel_noise = np.ones((6,6),np.uint8) #to delete small noises
#     # kernel_dilate = np.ones((30,30),np.uint8)  #bigger kernel to fill holes after ropes
#     # kernel_erode = np.ones((38,38),np.uint8)  #bigger kernel to delete pixels on edge that was add after dilate function

#     # imgErode = cv2.erode(lower_mask, kernel_noise, 1)
#     # imgDilate = cv2.dilate(imgErode , kernel_dilate, 1)
#     # imgErode = cv2.erode(imgDilate, kernel_erode, 1)
#     # cv2.imshow("cleaned foreground", imgErode)

#     contours, _ = cv2.findContours(lower_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     if len(contours) == 0:
#         return

#     largest_contour = max(contours, key=cv2.contourArea)

#     mask = np.zeros_like(lower_mask)
#     cv2.drawContours(mask, [largest_contour], -1, (255), thickness=cv2.FILLED)

#     M = cv2.moments(largest_contour)

#     if M["m00"] == 0:
#         return

#     cX = int(M["m10"] / M["m00"])
#     cY = int(M["m01"] / M["m00"])
#     cv2.circle(mask, (cX, cY), 70, (0, 0, 0), -1) # draw circle in middle of toats
#     cv2.imwrite("OUTPUT.png", mask)

#     return cX, cY, time.time()

