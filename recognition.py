import cv2

image = cv2.imread('images/people_2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('AI-learning/faces.xml') # Суть метода: вытягивает определенный файл (натренированную модель)

#scaleFactor - можем находить лица, которые в 2 раза больше, чем модель тренировала
#minNeighbors - как много объектов может быть рядом друг с другом
results = faces.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5) # Находим координаты всех найденных объектов (лиц)

for (x, y, w, h) in results:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)
        
cv2.imshow('Result', image)
cv2.waitKey(0)
    