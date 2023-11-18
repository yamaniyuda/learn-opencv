import os
import cv2

img_path = os.path.join(os.path.dirname( __file__ ), '..', '_data', 'people.jpeg')
img = cv2.imread(img_path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow('img', img)
cv2.imshow('img rgb', img_rgb)
cv2.waitKey(0)