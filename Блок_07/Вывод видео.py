import cv2


cap = cv2.VideoCapture(0)
while True:
    key = cv2.waitKey(1)
    if key == 27:
        break
    ret, img = cap.read()
    cv2.imshow('Image', img)