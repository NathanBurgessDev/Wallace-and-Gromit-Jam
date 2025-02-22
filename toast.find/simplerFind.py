import numpy as np
import cv2

src = cv2.imread('image1.jpeg')
imgRGB = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

lower = np.array([20, 0, 0])
upper = np.array([100, 255, 255])
imgRange = cv2.inRange(imgHSV, lower, upper)
cv2.imshow("green part of image", imgRange)

imgForeground = cv2.bitwise_not(imgRange)
cv2.imshow("foreground", imgForeground)

#kernels for morphology operations
kernel_noise = np.ones((3,3),np.uint8) #to delete small noises
kernel_dilate = np.ones((30,30),np.uint8)  #bigger kernel to fill holes after ropes
kernel_erode = np.ones((38,38),np.uint8)  #bigger kernel to delete pixels on edge that was add after dilate function

imgErode = cv2.erode(imgForeground, kernel_noise, 1)
imgDilate = cv2.dilate(imgErode , kernel_dilate, 1)
imgErode = cv2.erode(imgDilate, kernel_erode, 1)
cv2.imshow("cleaned foreground", imgErode)

contours, _ = cv2.findContours(imgErode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the largest contour by area
largest_contour = max(contours, key=cv2.contourArea)

# Create a mask for the largest region
mask = np.zeros_like(imgErode)
cv2.drawContours(mask, [largest_contour], -1, (255), thickness=cv2.FILLED)

# Show result
cv2.imshow("Largest Region", mask)



cv2.waitKey(0)
cv2.destroyAllWindows()