import cv2
import numpy as np

# !!! ПРИМЕЧАНИЕ:
# Благодаря библиотеке Numpy мы можем легко создавать матрицы

image = cv2.imread('images/photo_1.jpg')

# Отзеркаливание: 
# image = cv2.flip(image, -1) # Отображение
# END

def rotate(image_param, angle):
    height, width = image_param.shape[:2]
    point = (width // 2, height // 2)
    
    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(image_param, mat, (height, width))

# image = rotate(image, -50)

def transform(image_param, x, y):
    mat = np.float32([
        [1, 0, x], [0, 1, y] # По x = 0; по y = 1, по z = x 
    ])
    
    print(mat)
    
    return cv2.warpAffine(image_param, mat, (image_param.shape[1], image_param.shape[0]))

image = transform(image, 30, 200)

cv2.imshow('Результат', image)

cv2.waitKey(0)