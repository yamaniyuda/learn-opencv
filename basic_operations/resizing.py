import cv2
import os

img = cv2.imread(os.path.join('.', 'data', 'people.jpeg'))
resize_image = cv2.resize(img, (400, 400))

print(img.shape)
print(resize_image.shape)

cv2.imshow('people', img)
cv2.imshow('resize_people', resize_image)
cv2.waitKey(0)