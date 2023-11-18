import os
import cv2

# read
video_path = os.path.join('.', 'data', 'she.webm')
video = cv2.VideoCapture(video_path)

read = True
while read:
  read, frame = video.read()

  if read:
    cv2.imshow('frame', frame)
    cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()