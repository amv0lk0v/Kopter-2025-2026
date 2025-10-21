from pioneer_sdk import Pioneer
import time
def wait():
    while not drone.point_reached():
        pass
drone = Pioneer()
while True:
    drone.led_control(led_id=255, r=1, g=1, b=1)
    drone.led_control(led_id=255, r=0, g=0, b=0)
    time.sleep(1)


'''finally:
    drone.land()
    drone.disarm()'''