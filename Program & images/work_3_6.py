import cv2
import numpy as np

img = cv2.imread('tomatoes.png', 1)
cv2.imshow("original", img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
res, thresh = cv2.threshold(hsv[:, :, 0], 25, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("thresh", thresh)

edges = cv2.Canny(img, 100, 200, apertureSize=3)
cv2.imshow("canny", edges)

# inverting edges
edge_inv = 255 - edges

# erosion to increase size of border
kernal = np.ones((3,3), 'uint8')
erode = cv2.erode(edge_inv, kernal, iterations=1)

# combining threshold and erode
canny_thresh = cv2.bitwise_and(erode, thresh)
cv2.imshow("canny thresh", canny_thresh)

# contours detection
contours, hierarchy = cv2.findContours(canny_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

objects = img.copy()
for c in contours:
	area = cv2.contourArea(c)
	if area < 300:
		# too small area is neglected
		continue

	print("Area", area)
	# finding centroids
	cv2.drawContours(objects, [c], -1, (255,255,255), 1)
	M = cv2.moments(c)
	cx = int(M['m10'] / M['m00'])
	cy = int(M['m01'] / M['m00'])
	cv2.circle(objects, (cx, cy), 3, (255,255,0), -1)

cv2.imshow("final draw-over", objects)

cv2.waitKey(0)
cv2.destroyAllWindows()