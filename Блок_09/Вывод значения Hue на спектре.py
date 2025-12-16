import numpy, cv2

height, width = 300, 3*255
img = numpy.zeros((height, width, 3), numpy.uint8)
c = 0

external_x = 0


def mouse_event(event, x, y, flags, userdata):
    global external_x
    external_x = x
    print(external_x)

for i in range(0, width, 3):
    img[0:height, i:i+3] = (c, 255, 255)
    c += 1

img = cv2.cvtColor(img,70)
cv2.imshow('Image', img)

copy = img.copy()

print('Нажми Esc, чтобы закрыть окно')
while True:
    cv2.setMouseCallback('Image', mouse_event)
    cv2.putText(img, f"{external_x // 3}", [0, 30], cv2.FONT_HERSHEY_PLAIN, 2, [0, 0, 0], 2)
    img[0:height, external_x:external_x + 3] = (0, 0, 0)
    cv2.imshow('Image', img)
    img = copy.copy()
    key = cv2.waitKey(1)
    if key == 27:
        break