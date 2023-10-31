import cv2
import numpy as np

image = cv2.imread('images/photo_4.jpg')
image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
photo = np.zeros(image.shape, dtype='uint8')

image = cv2.GaussianBlur(image, (3, 3), 0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.Canny(image, 80, 90)

contour, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(photo, contour, -1, (127, 255, 212), thickness=1)

photo = cv2.cvtColor(photo, cv2.COLOR_RGB2BGR)

cv2.imshow('Result', photo)
cv2.waitKey(0)