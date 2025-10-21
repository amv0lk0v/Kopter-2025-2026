from pioneer_sdk import Pioneer
drone = Pioneer()
def wait():
    while not drone.point_reached():
        drone.led_control(led_id=255, r = r, g = g, b = b)
        pass
r, g, b = 1, 0, 0
try:
    drone.arm()
    drone.takeoff()

    drone.go_to_local_point_body_fixed(0, 0, 1, 0)
    wait()

    r, g, b = 1, 0, 0
    drone.go_to_local_point_body_fixed(0, 1, 0, 0)
    wait()
    r, g, b = 1, 0.5, 0
    drone.go_to_local_point_body_fixed(-1, 0, 0, 0)
    wait()
    r, g, b = 1, 1, 0
    drone.go_to_local_point_body_fixed(0, -1, 0, 0)
    wait()
    r, g, b = 0, 1, 0
    drone.go_to_local_point_body_fixed(1, 0, 0, 0)
    wait()

finally:
    drone.land()
    drone.disarm()
    drone.led_control(led_id=255, r=0, g=0, b=0)