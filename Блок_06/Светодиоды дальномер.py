from pioneer_sdk import Pioneer
import random
def wait():
    while not drone.point_reached():
        pass
drone = Pioneer()

try:
    drone.arm()
    drone.takeoff()
    drone.go_to_local_point_body_fixed(0, 0, 1.5, 0)
    wait()
    while True:
        a = drone.get_dist_sensor_data(get_last_received=True)
        while a == None:
            a = drone.get_dist_sensor_data(get_last_received=True)
            continue
        if a < 0.5:
            color = (0, 0.2, 0.4, 0.6, 0.8, 1)
            r, g, b = random.choice(color), random.choice(color), random.choice(color)
            drone.led_control(led_id=255, r=r, g=g, b=b)



finally:
    drone.land()
    drone.disarm()
    drone.led_control(led_id=255, r=0, g=0, b=0)