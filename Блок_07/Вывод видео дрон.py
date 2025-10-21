from pioneer_sdk import Camera
import cv2
camera = Camera()

while True:
    key = cv2.waitKey(1)
    if key == 27:
        break
    img = camera.get_cv_frame()
    if img is not None:
        cv2.imshow('Image', img)