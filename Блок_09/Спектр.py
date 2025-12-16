import numpy, cv2

height, width = 100, 3*255
img = numpy.zeros((height, width, 3), numpy.uint8)
c = 0

for i in range(0, width, 3):
    img[0:height, i:i+3] = (c, 255, 255)
    c += 1

img = cv2.cvtColor(img,70)

cv2.imshow('Image', img)

print('Нажми Esc, чтобы закрыть окно')
while True:
    key = cv2.waitKey(1)
    if key == 27:
        break