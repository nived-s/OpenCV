import numpy as np
import cv2

color = cv2.imread("butterflies.jpg", 1)

gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)  # converts to greyscale
cv2.imwrite("grey.jpg", gray)                   # writes 'grey' to grey.jpg

# transparancy or alpha channel
b = color[:, :, 0]
g = color[:, :, 1]
r = color[:, :, 2]

rgba = cv2.merge((b, g, r, g))          # 4th argument 'g' is the alpha channel, it highlights all green colours to transparant
cv2.imwrite("rgba.png", rgba)           # jpg does not support 4th chanel which is transparency so we use png for transparency proprty

