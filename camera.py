import cv2

capture = cv2.VideoCapture(0) # Считываем веб-камеру
capture.set(3, 500) # Размер видео: id-3 - ширина
capture.set(4, 300) # Размер видео: id-4 - высота


while True:
    success, image = capture.read()
    cv2.imshow('Result', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break