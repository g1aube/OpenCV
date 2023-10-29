import cv2
import numpy as np

# МАТРИЦА:

# [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]

photo = np.zeros((300, 300, 3), dtype='uint8') # 3 слоя - сможем окрашивание делать: стоит почитать в документации о всех слоях

# RGB - стандарт
# BGR - формат в OpenCV

# photo[:] = 100, 255, 0 # Все изображение
# photo[100:150, 200:280] = 100, 255, 0 # ОТ 100 ПИКСЕЛЯ ДО 150 по высоте и ОТ 200 ПИКСЕЛЯ ДО 280 по ширине

# Также можно использовать методы OpenCV

cv2.rectangle(photo, (50, 50), (100, 100), (100, 255, 0), thickness=3)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (100, 255, 0), thickness=3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 100, (100, 255, 0), thickness=cv2.FILLED) # 100 - радиус круга

cv2.putText(photo, 'yakummi', (100, 70), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), thickness=3)

cv2.imshow('Result:', photo)

cv2.waitKey(0)