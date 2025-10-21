from pioneer_sdk import Pioneer
drone = Pioneer()
def wait():
    while not drone.point_reached():
        pass

try:
    drone.arm()
    drone.takeoff()
    drone.go_to_local_point_body_fixed(0, 0, 1, 0)
    wait()

    for _ in range(5):
        drone.go_to_local_point_body_fixed(0, 1, 0, 0)
        wait()
        drone.go_to_local_point_body_fixed(0, 0, 0, -2.71)
        wait()


finally:
    drone.land()
    drone.disarm()