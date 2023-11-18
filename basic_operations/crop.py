import os
import cv2

img_path = os.path.join(os.path.dirname( __file__ ), '..', '_data', 'people.jpeg')
img = cv2.imread(img_path)

croper_img = img[300:600, 300:600]

cv2.imshow('image', img)
cv2.imshow('croper image', croper_img)
cv2.waitKey(0)