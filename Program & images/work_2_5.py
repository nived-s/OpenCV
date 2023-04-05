import numpy as np
import cv2

img = cv2.imread("kitten.jpg", 1)
cv2.imshow("Original", img)

# scale
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img_stretch = cv2.resize(img, (600,600))
img_stretch_near = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half", img_half)
cv2.imshow("Strech", img_stretch)
cv2.imshow("Strech near", img_stretch_near)

# rotaion
M = cv2.getRotationMatrix2D((0,0), -30, 1)					# (x and y coord of from where to rotate), degree
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))		# shape of image is passed it will be to resolution of window
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()