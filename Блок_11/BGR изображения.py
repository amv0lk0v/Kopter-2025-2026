import cv2
print('Нажми Esc, чтобы закрыть видео')
cap = cv2.VideoCapture(0)

while True:
    key = cv2.waitKey(1)
    if key == 27:
        break

    ret, img = cap.read()
    img = cv2.cvtColor(img, 66)
    maskb = cv2.inRange(img, (40, 0, 0), (125, 255, 255))
    maskg = cv2.inRange(img, (125, 0, 0), (210, 255, 255))
    maskr = cv2.inRange(img, (-40, 0, 0), (45, 255, 255))

    new_imageb = cv2.bitwise_and(img, img, mask=maskb)
    new_imageg = cv2.bitwise_and(img, img, mask=maskg)
    new_imager = cv2.bitwise_and(img, img, mask=maskr)

    img = cv2.cvtColor(img, 70)
    new_imageb = cv2.cvtColor(new_imageb, 70)
    new_imageg = cv2.cvtColor(new_imageg, 70)
    new_imager = cv2.cvtColor(new_imager, 70)
    cv2.imshow('Image', img)
    cv2.imshow('Mask_Imageb', new_imageb)
    cv2.imshow('Mask_Imageg', new_imageg)
    cv2.imshow('Mask_Imager', new_imager)
    print(f'{maskb.sum()//255} / {480*640}')
    print(f'{maskg.sum() // 255} / {480 * 640}')
    print(f'{maskr.sum() // 255} / {480 * 640}')