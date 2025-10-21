import cv2

key = ''
img = cv2.imread("img.jpg")
cv2.imshow('Image', img)

while not key == ord('q'):
    key = cv2.waitKey(0)