import cv2
print('Нажми Esc, чтобы закрыть видео')
cap = cv2.VideoCapture(0)
while True:
    key = cv2.waitKey(1)
    if key == 27:
        break
    ret, img = cap.read()

    image = img[290:350, 220:280]
    image = cv2.resize(image, None, fx=2, fy=2)

    cv2.rectangle(img, [220, 290], [280, 350], [0, 0, 255])
    cv2.imshow('Image', img)
    cv2.imshow('BigImage', image)