from pioneer_sdk import Pioneer
drone = Pioneer()
def wait():
    while not drone.point_reached():
        pass
    drone.led_control(led_id=255, r=1, g=1, b=1)
    drone.led_control(led_id=255, r=0, g=0, b=0)
try:
    drone.arm()
    drone.takeoff()
    drone.go_to_local_point_body_fixed(0, 0, 1, 0)
    wait()

    drone.go_to_local_point_body_fixed(0, 1, 0, 0)
    wait()
    drone.go_to_local_point_body_fixed(-1, 0, 0, 0)
    wait()
    drone.go_to_local_point_body_fixed(0, -1, 0, 0)
    wait()
    drone.go_to_local_point_body_fixed(1, 0, 0, 0)
    wait()

finally:
    drone.land()
    drone.disarm()