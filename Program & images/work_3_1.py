import cv2
import numpy as np

bw = cv2.imread('bw_binary.png', 0)			# 0 to load in bw
height, width = bw.shape[0:2]
cv2.imshow("original BW", bw)

binary = np.zeros([height, width, 1], 'uint8')

thresh = 100	# threshold

for row in range(0, height):
	for col in range(0, width):
		if bw[row][col] > thresh:
			binary[row][col] = 255

cv2.imshow("slow binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()