from pioneer_sdk import Pioneer
def wait():
    while not drone.point_reached():
        pass
drone = Pioneer()
while True:
    print(drone.get_dist_sensor_data(get_last_received=True))
