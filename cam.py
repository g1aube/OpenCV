import cv2
import numpy as np


capture = cv2.VideoCapture(0)

# =======
capture.set(3, 300)
capture.set(4, 300)
# =======

while True:
    success, image = capture.read()
    image_color = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_color = cv2.Canny(image_color, 30, 30)
    
    cv2.imshow('Результат', image_color)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    