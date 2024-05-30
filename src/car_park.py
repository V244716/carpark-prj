from sensor import Sensor
from display import Display
class CarPark:
    def __init__(self, location, capacity, plates = None, sensors = None, displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Car park at '{self.location}' contains '{self.capacity}' bays."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        if isinstance(component, Display):
            self.displays.append(component)







