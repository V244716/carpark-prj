from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json


class CarPark:
    def __init__(self, location, capacity, plates = None, sensors = None, displays = None, log_file=Path('log.txt'), config_file=Path('config.json')):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the log file if it doesn't exist:
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        # create the config file if it doesn't exist:
        self.config_file.touch(exist_ok=True)

    def _log_car_activity(self, plate, action):
        with self.log_file.open('a') as file:
            file.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

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
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")


    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays,
                            "Temperature": 42,}
                           )
            print(f"Updating {display}")

    def write_config(self):
        with open(self.config_file, "w") as file:  # TODO: use self.config_file; use Path; add optional parm to __init__
            json.dump({'location': self.location,
                       'capacity': self.capacity,
                       'log_file': str(self.log_file)}, file)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])
