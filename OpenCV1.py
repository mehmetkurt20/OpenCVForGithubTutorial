import cv2
import numpy as np

img = cv2.imread("Example.png")
#cv2.imshow("Image",img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray",gray)

#Simple Thresholding
threshold, thresh = cv2.threshold(gray, 140,255, cv2.THRESH_BINARY)
#cv2.imshow("Simple Thresholded", thresh)

#Inversed Simple Thresholding
threshold, thresh_inv = cv2.threshold(gray, 140,255, cv2.THRESH_BINARY_INV)
#cv2.imshow("Simple Inversed Thresholded", thresh_inv)

#Adaptive Threshold
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 1)
#cv2.imshow("Adaptive Thresholding", adaptive_thresh)

#Erosion And Dilation Examples
img2 = cv2.imread("Example.png")

kernel=np.ones((3,3),np.uint8)
kernel2=np.ones((5,5),np.uint8)

eroded=cv2.erode(img2,kernel,iterations=3)
#cv2.imshow("Eroded", eroded)

dilated=cv2.dilate(eroded,kernel2,iterations=3)
#cv2.imshow("Dilated",dilated)

#cv2.waitKey(0)
