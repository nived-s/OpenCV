import cv2
import numpy as np

# template matching

template = cv2.imread("template.jpg", 0)		# reading in grayscale
frame = cv2.imread("players.jpg", 0)		# reading in grayscale

cv2.imshow("frame", frame)
cv2.imshow("template", template)

result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(min_val, max_val)

cv2.circle(result, max_loc, 15, 255, 2)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()