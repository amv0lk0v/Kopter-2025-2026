from pioneer_sdk import Camera, Pioneer

drone = Pioneer()


try:
    time = 10
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
        print(ch_1, ch_2, ch_3, ch_4, ch_5, '|', dist)
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

    for _ in range(1):

        #Начало движения по окружности
        for x in range(0, -101, -1):
            dist = drone.get_dist_sensor_data(get_last_received=True)
            y = -1 * (10_000 - x ** 2) ** 0.5
            ch_4 = int(1500 + x)  # вправо, влево
            ch_3 = int(1500 + y)  # вперёд, назад
            if dist < 0.8:
                ch_1 = 1590
            if dist > 0.9:
                ch_1 = 1410
            print(ch_1, ch_2, ch_3, ch_4, ch_5, '|', dist)
            for _ in range(time):
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

        print('█')

        for x in range(-100, 1):
            dist = drone.get_dist_sensor_data(get_last_received=True)
            y = (10_000 - x ** 2) ** 0.5
            ch_4 = int(1500 + x)  # вправо, влево
            ch_3 = int(1500 + y)  # вперёд, назад
            if dist < 0.8:
                ch_1 = 1590
            if dist > 0.9:
                ch_1 = 1410
            print(ch_1, ch_2, ch_3, ch_4, ch_5, '|', dist)
            for _ in range(time):
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

        print('█')

        for x in range(0, 101):
            dist = drone.get_dist_sensor_data(get_last_received=True)
            y = (10_000 - x ** 2) ** 0.5
            if dist < 0.8:
                ch_1 = 1590
            if dist > 0.9:
                ch_1 = 1410
            ch_4 = int(1500 + x)  # вправо, влево
            ch_3 = int(1500 + y)  # вперёд, назад
            print(ch_1, ch_2, ch_3, ch_4, ch_5, '|', dist)
            for _ in range(time):
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

        print('█')

        for x in range(100, -1, -1):
            dist = drone.get_dist_sensor_data(get_last_received=True)
            y = -1 * (10_000 - x ** 2) ** 0.5
            ch_4 = int(1500 + x)  # вправо, влево
            ch_3 = int(1500 + y)  # вперёд, назад
            if dist < 0.8:
                ch_1 = 1590
            if dist > 0.9:
                ch_1 = 1410
            print(ch_1, ch_2, ch_3, ch_4, ch_5, '|', dist)
            for _ in range(time):
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

        print('█')


finally:
    drone.land()
    drone.disarm()