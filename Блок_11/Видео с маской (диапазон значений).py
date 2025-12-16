import cv2, numpy

def mouse_event(event, x, y, flags, userdata):
    global external_x, external_flags
    external_x = x
    external_flags = flags
def video():
    clmx = (max(x1, x2)//3, 255, 255)
    clmn = (min(x1, x2)//3, 0, 0)
    ret, img = cap.read()
    img = cv2.cvtColor(img, 66)
    mask = cv2.inRange(img, clmn, clmx)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    img = cv2.cvtColor(img, 70)
    new_image = cv2.cvtColor(new_image, 70)
    cv2.imshow('Image', img)
    cv2.imshow('Mask_Image', new_image)

print('Нажми Esc, чтобы закрыть видео')
cap = cv2.VideoCapture(0)


c = 0
height, width = 300, 3*255
external_x = 0
external_flags = 0b0
spector = numpy.zeros((height, width, 3), numpy.uint8)
x1, x2 = 0, 1000

for i in range(0, width, 3):
    spector[0:height, i:i+3] = (c, 255, 255)
    c += 1

spector = cv2.cvtColor(spector,70)
copy = spector.copy()
cv2.imshow('Spector', spector)
cv2.setMouseCallback('Spector', mouse_event)

exit_while = True

while exit_while:
    while True:
        if external_flags & cv2.EVENT_FLAG_LBUTTON:
            break
        key = cv2.waitKey(1)
        if key == 27:
            exit_while = False
            break
        video()
    spector[0:height, external_x:external_x + 3] = (0, 0, 0)
    x1 = external_x
    cv2.imshow('Spector', spector)

    while True:
        if not external_flags & cv2.EVENT_FLAG_LBUTTON:
            break
        key = cv2.waitKey(1)
        if key == 27:
            exit_while = False
            break
        video()

    spector[0:height, external_x:external_x + 3] = (0, 0, 0)
    x2 = external_x
    cv2.imshow('Spector', spector)

    spector = copy.copy()
    print(f'Ты выбрал диапазон от {min(x1, x2)//3} до {max(x1,x2)//3}')