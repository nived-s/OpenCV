import numpy as np
import cv2

cap = cv2.VideoCapture(0)

color = (0, 255,0)
line_width = 3						# -1 indicates filled figure
radius = 100
point = (100, 100)						# center location

def click(event, x, y, flags, param):
	global point, pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		print("pressed", x, y)
		point = (x, y)

cv2.namedWindow("LiveCam")
cv2.setMouseCallback("LiveCam", click)


while (True):
	ret, frame = cap.read()

	frame = cv2.resize(frame, (0, 0), fx=1.0, fy=1.0)
	cv2.circle(frame, point, radius, color, line_width)
	cv2.imshow("LiveCam", frame)

	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()