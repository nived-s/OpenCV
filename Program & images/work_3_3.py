import cv2
import numpy as np

img = cv2.imread('skin_detec_1.jpg', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]
cv2.imshow("original", img)

hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imshow("hsv split", hsv_split)

ret, min_sat = cv2.threshold(s, 50, 255, cv2.THRESH_BINARY)
cv2.imshow("saturation filter", min_sat)

ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY)
cv2.imshow("hue filter", max_hue)

# combing hue and sat filters
final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("final", final)

cv2.waitKey(0)
cv2.destroyAllWindows()
