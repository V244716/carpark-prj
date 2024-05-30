class Sensor:
    """Provides sensors to detect cars"""
    def __init__(self, id, car_park, is_active = False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"'{self.id}': Sensor is {'is active' if self.is_active else 'is inactive'}"

class EntrySensor(Sensor):
    pass

class ExitSensor(Sensor):
    pass


