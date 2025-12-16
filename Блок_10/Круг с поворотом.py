from pioneer_sdk import Camera, Pioneer
import cv2

drone = Pioneer()
img = cv2.imread("img.jpg")
cv2.imshow('Image', img)

try:
    for i in range(100):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000

        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

    ch_1 = 1500
    ch_2 = 1500
    ch_3 = 1500
    ch_4 = 1500
    ch_5 = 2000

    drone.arm()

    while True:
        dist = drone.get_dist_sensor_data(get_last_received=True)
        ch_1 = 1600
        if dist > 0.5:
            break
        print(ch_1, ch_2, ch_3, ch_4, ch_5)
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

    while True:
        key = cv2.waitKey(1)
        dist = drone.get_dist_sensor_data(get_last_received=True)

        if key == 27:
            break
        if dist < 0.8:
            ch_1 = 1600
        if dist > 0.9:
            ch_1 = 1400

        ch_2 = 1650 #поворот влево
        ch_3 = 1400 #вперёд
        print(ch_1, ch_2, ch_3, ch_4, ch_5)
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

    drone.land()

finally:
    drone.land()
    drone.disarm()