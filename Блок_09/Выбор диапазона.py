import numpy, cv2

height, width = 300, 3*255
spector = numpy.zeros((height, width, 3), numpy.uint8)
c = 0

external_x = 0
external_flags = 0b0


def mouse_event(event, x, y, flags, userdata):
    global external_x, external_flags
    external_x = x
    external_flags = flags
    #print(external_x, external_flags)

for i in range(0, width, 3):
    spector[0:height, i:i+3] = (c, 255, 255)
    c += 1

spector = cv2.cvtColor(spector,70)
copy = spector.copy()
cv2.imshow('Image', spector)
cv2.setMouseCallback('Image', mouse_event)

print('Нажми Esc, чтобы закрыть окно')

while True:
    while True:
        if external_flags & cv2.EVENT_FLAG_LBUTTON:
            break
        key = cv2.waitKey(1)
    spector[0:height, external_x:external_x + 3] = (0, 0, 0)
    x1 = external_x
    cv2.imshow('Image', spector)

    while True:
        if not external_flags & cv2.EVENT_FLAG_LBUTTON:
            break
        key = cv2.waitKey(1)

    spector[0:height, external_x:external_x + 3] = (0, 0, 0)
    x2 = external_x
    cv2.imshow('Image', spector)

    spector = copy.copy()
    print(f'Ты выбрал диапазон от {min(x1, x2)//3} до {max(x1,x2)//3}')