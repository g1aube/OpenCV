from matplotlib import pyplot as pl
import cv2
import numpy as np
import imutils
import easyocr


image = cv2.imread('images/car_5.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Уменьшаем шум (оптимизируем картинку)
image_filter = cv2.bilateralFilter(gray, 11, 15, 15) 
edges = cv2.Canny(image_filter, 30, 200)

contours = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours) # Считываем контуры
contours = sorted(contours, key=cv2.contourArea, reverse=True) # Сортируем контуры, ищем квадратные контуры, типо крупные контуры в конце списка будут и нам они нужны, потому что они будут явно намекать на номерной знак автомобиля

position = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True) # Приблизительно находим номерной знак наша форма может быть даже кругом (1) 2 - ближе к квадрату и т.д; True я написал - мы находим только ЗАКРЫТЫЕ контуры
    if len(approx) == 4: # 4 координаты 4 углов нашего квадрата
        position = approx
        break

mask = np.zeros(gray.shape, dtype=np.uint8)
new_image = cv2.drawContours(mask, [position], 0, 255, -1)
bitwise_image = cv2.bitwise_and(image, image, mask=mask)

(x, y) = np.where(mask == 255) # Те цвета, которые будут приближены к белому - будут вытянуты 
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
crop = gray[x1:x2, y1:y2]

# Читаем информацию с номерного знака:
text = easyocr.Reader(['en'], verbose=False)
text = text.readtext(crop)

# Выводим полученный номерной знак под нашим фото
result = text[0][-2]
print(result)
final_image = cv2.putText(image, result, (x1, y2 - 60), cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(0, 255, 255), thickness=1) # x1 - верхняя левая точка, y2 - нижняя точка 

pl.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
pl.show()