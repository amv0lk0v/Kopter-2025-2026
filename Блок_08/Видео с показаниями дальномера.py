from pioneer_sdk import Camera, Pioneer
import cv2
camera = Camera()
drone = Pioneer()


while True:
    p = drone.get_dist_sensor_data(get_last_received=True)
    key = cv2.waitKey(1)
    if key == 27:
        break
    img = camera.get_cv_frame()
    if img is not None:
        cv2.putText(img, f'Rangefinder readings: {p}', [0, 30], cv2.FONT_HERSHEY_PLAIN, 2, [255, 0, 0], 3)
        cv2.imshow('Image', img)