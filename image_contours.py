import cv2
import numpy as np

# Если мы блюрим изображение - мы сглаживаем углы!

image = cv2.imread('images/photo_2.jpg')

new_image = np.zeros(image.shape, dtype='uint8') # Создаем новое полотно с размерами основной картинки.

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.GaussianBlur(image, (5, 5), 0)

image = cv2.Canny(image, 100, 110) # Все цвета до 100 (99) будут проигнорированы и будут установлены как черный цвет (к нулю приведены), все цвета от 140 - белому

# В первую переменную будет установлен список со всеми контурами, со всеми позициями контуров, а во вторую иерархию самих объектов
# RETR_LIST - получаем уже все контуры, и мы обязательно должны были до этого действия сделать Canny
# CHAIN_APPROX_NONE - найдены все координаты всех контуров
contour, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # Рисуем контуры, полученные из нашей картинки

cv2.drawContours(new_image, contour, -1, (112, 34, 70), thickness=1)

cv2.imshow('Result', new_image)
cv2.waitKey(0)