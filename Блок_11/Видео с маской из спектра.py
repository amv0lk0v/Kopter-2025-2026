import cv2
print('Нажми Esc, чтобы закрыть видео')
cap = cv2.VideoCapture(0)

color = [140, 80, 90]
accuracy = 30
clmx = tuple([i + accuracy for i in color if i + accuracy <= 255])
clmn = tuple([i - accuracy  for i in color if i - accuracy >= 0])
print(color)

while True:
    key = cv2.waitKey(1)
    if key == 27:
        break
    ret, img = cap.read()
    mask = cv2.inRange(img, clmn, clmx)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Image', img)
    cv2.imshow('Mask_Image', new_image)