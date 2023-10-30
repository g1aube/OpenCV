import cv2
import numpy as np

photo = cv2.imread('images/photo_1.jpg')
image = np.zeros((photo.shape[:2]), dtype='uint8')
# image = np.zeros((350, 350), dtype='uint8')

circle = cv2.circle(img=image.copy(), center=(200, 300), radius=120, color=255, thickness=-1|cv2.FILLED)
rectangle = cv2.rectangle(img=image.copy(), pt1=(25, 25), pt2=(250, 350), color=100, thickness=-1)

# БИТОВЫЕ ОПЕРАЦИИ, ОБЪЕДИНЕНИЕ:
image = cv2.bitwise_and(src1=photo, src2=photo, mask=circle)
# image = cv2.bitwise_or(src1=circle, src2=rectangle)
# image = cv2.bitwise_xor(src1=circle, src2=rectangle)
# image = cv2.bitwise_not(rectangle)

# Игот: Благодаря битовым операциям и маскам мы можем выделять только нужную нам часть картинки и работать с ней, нежели работать со всем изображением

cv2.imshow('Result', image)

cv2.waitKey(0)