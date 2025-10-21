from pioneer_sdk import Pioneer
import time
def wait():
    while not drone.point_reached():
        pass
drone = Pioneer()

try:
    drone.arm()
    drone.takeoff()
    drone.go_to_local_point_body_fixed(0, 0, 1.5, 0)
    wait()
    time.sleep(1)
    while drone.get_dist_sensor_data(get_last_received=True) >= 1:
        pass


finally:
    drone.land()
    drone.disarm()