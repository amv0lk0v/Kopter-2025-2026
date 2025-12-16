from pioneer_sdk import Camera, Pioneer
import cv2
import time

def cam(img, dist, key):
    if img is not None:
        cv2.putText(img, f'{dist}', [0, 30], cv2.FONT_HERSHEY_PLAIN, 2, [255, 0, 0], 3)
        cv2.putText(img, f'{key}', [0, 60], cv2.FONT_HERSHEY_PLAIN, 2, [255, 0, 0], 3)
        cv2.imshow('Image', img)

drone = Pioneer()
camera = Camera()

key = ''


try:
    for i in range(100):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

    while True:

        key = cv2.waitKey(1)
        dist = drone.get_dist_sensor_data(get_last_received=True)
        img = camera.get_cv_frame()

        cam(img, dist, key)

        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000

        if key == 27:
            break

        if key == ord('1'):
            drone.arm()
        if key == ord('2'):
            drone.disarm()

        if key == ord('3'):
            '''takeoff'''
            while True:
                img = camera.get_cv_frame()
                dist = drone.get_dist_sensor_data(get_last_received=True)
                if dist > 0.5:
                    break
                cam(img, dist, '3')
                ch_1 = 1600
                print(ch_1, ch_2, ch_3, ch_4, ch_5)
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)


        if key == ord('4'):
            '''land'''
            drone.land()

        if key == ord('w'):
            '''вперёд'''
            ch_3 = 1400
        if key == ord('s'):
            '''назад'''
            ch_3 = 1600
        if key == ord('a'):
            '''налево'''
            ch_4 = 1400
        if key == ord('d'):
            '''направо'''
            ch_4 = 1600
        if key == ord('q'):
            '''поворот влево'''
            ch_2 = 1600
        if key == ord('e'):
            '''поворот вправо'''
            ch_2 = 1400
        if key == ord('=') or key == ord('+'):
            '''вверх'''
            ch_1 = 1600
        if key == ord('-'):
            '''вниз'''
            ch_1 = 1400
        print(ch_1, ch_2, ch_3, ch_4, ch_5)
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

finally:
    drone.land()
    drone.disarm()