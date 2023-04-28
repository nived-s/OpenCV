import cv2
import numpy as np

img = cv2.imread('sudoku.jpg', 0)
cv2.imshow("original", img)

# basic threshold
ret, thresh_basic = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
cv2.imshow("basic threshold", thresh_basic)

# adaptive threshold
thresh_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
cv2.imshow("adaptiveThreshold", thresh_adapt)


cv2.waitKey(0)
cv2.destroyAllWindows()