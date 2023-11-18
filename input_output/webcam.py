import os
import cv2

# read
webcam = cv2.VideoCapture(0)

# visualiza webcam
while True:
  read, frame = webcam.read()

  cv2.imshow('frame', frame)
  if cv2.waitKey(40) & 0xFF == ord('q'):
    break

webcam.release()
cv2.destroyAllWindows()