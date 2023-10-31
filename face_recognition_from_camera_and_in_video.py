import cv2

def face_capture():

    cascade_path = 'AI-learning/new_faces.xml' 

    classifier = cv2.CascadeClassifier(cascade_path) # Строим классификатор на основе нашего обучения нейросети
    camera_path = 0
    camera = cv2.VideoCapture(camera_path)  # Захватываем видео-поток
    camera.set(3, 500) # Размер видео: id-3 - ширина
    camera.set(4, 300) # Размер видео: id-4 - высота

    while True:
        success, frame = camera.read() # Захватывает и декодирует нам кадры из видео
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Чтобы нейросеть работала хорошо - поменяем цветовую гамму на серую
        faces = classifier.detectMultiScale(
            image=gray,
            scaleFactor=1.1,
            minNeighbors=2,
            minSize=(30, 30), # Минимальное значение лица в пикселях по x и y
            flags=cv2.CASCADE_SCALE_IMAGE # Параметр с тем же значением для старого каскада. Он не используется для нового каскада! НЕ ОСОБО ВАЖНО!
        ) # Находим все лица на камере
        
        for (x, y, width, height) in faces: # Обводим лицо рамкой
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), thickness=2)
            
        cv2.imshow('Result', frame)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    camera.release()
    cv2.destroyAllWindows()
            
    
def main():
    face_capture()
    
if __name__ == '__main__':
    main()