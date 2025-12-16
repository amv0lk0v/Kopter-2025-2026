import cv2
print('Нажми Esc, чтобы закрыть видео')
cap = cv2.VideoCapture(0)
while True:
    key = cv2.waitKey(1)
    if key == 27:
        break
    ret, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Image', img)