import cv2
import numpy as np


image = cv2.imread('images/photo_1.jpg') # Читает изображение
# image_resize = cv2.resize(image, (1500, 1500))
image_resize = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2)) # В 2 раза меньше
image_resize = cv2.GaussianBlur(image_resize, (9, 9), 0) # размытие (x, x), y y - сигма, умножитель 
image_resize = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY) # изменение цвета, теперь серый слой

image_resize = cv2.Canny(image_resize, 30, 30) # Обведенно контуром, чем меньше значение - тем лучше обводится

# Создаем матрицу: 

kernel = np.ones((2, 2), np.uint8)

# END

image_resize = cv2.dilate(image_resize, kernel, iterations=1) # увеличиваем жирность обводок

image_resize = cv2.erode(image_resize, kernel, iterations=1) # Чтобы компу было лучше читать, уменьшили лишнее

# img[0:100, 0:150]
cv2.imshow('Result', image_resize) # Показываем изображение

# print(image.shape) # Размер картинки

# Запуск картинки: 
cv2.waitKey(0) # Картинка будет показываться бессконечное количество времени, пока я сам ее не остановлю
