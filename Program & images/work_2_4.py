import numpy as np
import cv2

image = cv2.imread("kitten.jpg", 1)
cv2.imshow("original", image)

# Gaussian blur
blur = cv2.GaussianBlur(image, (5,55), 0)       # x and y coordinates
cv2.imshow("after", blur)

#dilation and erosion
kernal = np.ones((5,5), 'uint8')				# x and y

dilate = cv2.dilate(image, kernal, iterations=1)
erode = cv2.erode(image, kernal, iterations=1)

cv2.imshow("Dilate", dilate)
cv2.imshow("Erosion", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()	