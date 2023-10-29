import cv2

capture = cv2.VideoCapture('videos/video_1.mp4') # Получаем видео

while True:
    success, image = capture.read() # Читаем видео: success - True|False, прочиталось ли видео или нет; image - кадры из видео
    cv2.imshow('Result', image)
    
    # С помощью q мы можем завершать программу
    if cv2.waitKey(1) & 0xFF == ord('q'): # waitkey(1) - с такой скоростью будут меняться кадры
        break
