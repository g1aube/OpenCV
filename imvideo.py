import cv2
import numpy as np

capture = cv2.VideoCapture('videos/video_1.mp4')

while True:
    success, image = capture.read()
    
    image = cv2.GaussianBlur(image, (9, 9), 0) # размытие (x, x), y y - сигма, умножитель 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # изменение цвета, теперь серый слой

    image = cv2.Canny(image, 10, 10) # Обведенно контуром, чем меньше значение - тем лучше обводится

    kernel = np.ones((2, 2), np.uint8)

    image = cv2.dilate(image, kernel, iterations=1) # увеличиваем жирность обводок

    image = cv2.erode(image, kernel, iterations=1) # Чтобы компу было лучше читать, уменьшили лишнее

    cv2.imshow('Result', image) # Показываем изображение
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

