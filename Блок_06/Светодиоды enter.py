from pioneer_sdk import Pioneer
import time
def wait():
    while True:
        input()
        break
drone = Pioneer()

try:
    while True:
        drone.led_control(led_id=255, r=0, g=0, b=0)
        wait()
        drone.led_control(led_id=255, r=1, g=0, b=0)
        wait()
        drone.led_control(led_id=255, r=1, g=0.5, b=0)
        wait()
        drone.led_control(led_id=255, r=1, g=1, b=0)
        wait()
        drone.led_control(led_id=255, r=0, g=1, b=0)
        wait()
        drone.led_control(led_id=255, r=0, g=0.9, b=0.8)
        wait()
        drone.led_control(led_id=255, r=0, g=0.6, b=1)
        wait()
        drone.led_control(led_id=255, r=0.5, g=0, b=0.7)
        wait()



finally:
    drone.led_control(led_id=255, r=0, g=0, b=0)