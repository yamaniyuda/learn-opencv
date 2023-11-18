import os
import cv2

# ============ Read Image ==========
image_path = os.path.join('.', 'data', 'people.jpeg')
img = cv2.imread(image_path)

# write image
cv2.imwrite(os.path.join('.', 'data', 'people_out.jpeg'), img)

# visualize image
cv2.imshow('people', img)
cv2.waitKey(0)



# ============== Video ==============
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


# ============= Web Cam =============
# read webcam
webcam = cv2.VideoCapture(0)

# visualiza webcam
while True:
  read, frame = webcam.read()

  cv2.imshow('frame', frame)
  if cv2.waitKey(40) & 0xFF == ord('q'):
    break

webcam.release()
cv2.destroyAllWindows()