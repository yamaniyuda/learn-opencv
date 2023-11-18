import os
import cv2

# read
image_path = os.path.join('.', 'data', 'people.jpeg')
img = cv2.imread(image_path)

# write 
cv2.imwrite(os.path.join('.', 'data', 'people_out.jpeg'), img)

# visualize
cv2.imshow('people', img)
cv2.waitKey(0)