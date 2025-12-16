from pioneer_sdk import Pioneer
drone = Pioneer()

try:
    for i in range(100):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

    drone.arm()
    while True:
        dist = drone.get_dist_sensor_data(get_last_received=True)
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        if dist < 1:
            ch_1 = 1600
        if dist > 1.1:
            ch_1 = 1430
        print(dist, ch_1)
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
finally:
    drone.land()
    drone.disarm()