from pioneer_sdk import Pioneer
import math
drone = Pioneer()

try:
    drone.arm()
    drone.takeoff()
    drone.go_to_local_point(0, 0, 0.5, 0)
    while not drone.point_reached():
        pass
    drone.go_to_local_point(0, 1, 0.5, 0)
    while not drone.point_reached():
        pass
    drone.go_to_local_point_body_fixed(0, 0, 0, -math.pi / 2)
    while not drone.point_reached():
        pass
    drone.go_to_local_point(-1, 1, 0.5, 0)
    while not drone.point_reached():
        pass
    drone.go_to_local_point_body_fixed(0, 0, 0, -math.pi / 2)
    while not drone.point_reached():
        pass
    drone.go_to_local_point(-1, 0, 0.5, 0)
    while not drone.point_reached():
        pass
    drone.go_to_local_point_body_fixed(0, 0, 0, -math.pi / 2)
    while not drone.point_reached():
        pass
    drone.go_to_local_point(0, 0, 0.5, 0)
    while not drone.point_reached():
        pass
    drone.go_to_local_point_body_fixed(0, 0, 0, -math.pi / 2)
    while not drone.point_reached():
        pass
    drone.land()
    drone.disarm()

finally:
    drone.land()