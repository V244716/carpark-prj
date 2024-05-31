from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location, capacity, plates = None, sensors = None, displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    @property
    def available_bays(self):
        # car_park.available_bays
        available = self.capacity - len(self.plates)
        if available < 0: available = 0
        return available

    def __str__(self):
        return f"Car park at '{self.location}' contains '{self.capacity}' bays."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        if isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()


    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays,
                            "Temperature": 42,}
                           )
            print(f"Updating {display}")


