import cv2
key = ('')

cap = cv2.VideoCapture(0)
ret, img = cap.read()

cv2.imshow('Image', img)

while not key == 27:
    key = cv2.waitKey(0)

img.release()