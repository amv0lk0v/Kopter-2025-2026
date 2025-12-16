import cv2
print('Нажми Esc, чтобы закрыть видео')
cap = cv2.VideoCapture(0)
ret, img = cap.read()
height, width, no = img.shape
height //= 2
width //= 2
print(height, width)

while True:
    key = cv2.waitKey(1)
    if key == 27:
        break

    ret, img = cap.read()
    image = cv2.resize(img, None, fx=0.5, fy=0.5)
    image1 = image
    image2 = cv2.flip(image, 1)
    image3 = cv2.flip(image, 0)
    image4 = cv2.flip(image, -1)
    img[0:height, 0:width] = image1[0:height, 0:width]
    img[0:height, width:2*width] = image2[0:height, 0:width]
    img[height:2*height, 0:width] = image3[0:height, 0:width]
    img[height:2*height, width:2*width] = image4[0:height, 0:width]
    cv2.imshow('Image', img)
print(img.shape)