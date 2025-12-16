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
    drone.go_to_local_point_body_fixed(-0.3, 0.95, 0, 0)
    wait()
    drone.go_to_local_point_body_fixed(-0.3, -0.95, 0, 0)
    wait()
    drone.go_to_local_point_body_fixed(0.8, 0.59, 0, 0)
    wait()
    drone.go_to_local_point_body_fixed(-1, 0, 0, 0)
    wait()
    drone.go_to_local_point_body_fixed(0.8, -0.59, 0, 0)
    wait()


finally:
    drone.land()
    drone.disarm()