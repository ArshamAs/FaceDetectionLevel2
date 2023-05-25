import cv2
import easygui
from PIL import Image

path = easygui.fileopenbox()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img2 = cv2.imread(path)
img = cv2.resize(img2,(1080,720))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
   cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()