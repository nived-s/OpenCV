import numpy as np
import cv2

"""img = cv2.imread("car.png", 1)
cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Image", img)
cv2.waitKey(0)
# cv2.imwrite("output.jpg", img)
print(img)
print(type(img))
print(len(img))
print(img.dtype)
print(img.shape)"""


black = np.zeros([250,250,1], 'uint8')
cv2.imshow("Black", black)

ones = np.ones([250,250,3], 'uint8')
cv2.imshow("Ones", ones)

white = np.ones([250,250,3], 'uint16')
white *= (2**16-1)              #multiply all 1 ones by 255
cv2.imshow("White", white)

color = ones.copy()             #copy ones but no linked
color[:,:] = (255,0,0)          #giving color value to each elemetn of array 
cv2.imshow("Blue", color)       #BGR format


cv2.waitKey(0)
cv2.destroyAllWindows()
