from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
moondalup_car_park = CarPark('moondalup', 100, log_file='moondalup.txt')
moondalup_car_park.write_config()


# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(1, moondalup_car_park, True)


# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(2, moondalup_car_park, True)


# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park

display = Display(1, moondalup_car_park, "", True)


# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for car in range(10):
    rego = entry_sensor._scan_plate()
    entry_sensor.update_car_park(rego)


# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for car in range(2):
    rego = exit_sensor._scan_plate()
    exit_sensor.update_car_park(rego)




# create a car park
# detect a car
# output to the display
# detect a car leaving
# THE END

