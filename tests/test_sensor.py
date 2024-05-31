import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("90 William Street", 50)
        self.entry_sensor = EntrySensor(5, self.car_park, is_active=True)
        self.exit_sensor = ExitSensor(10, self.car_park, is_active=True)

    def test_entry_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 5)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

    def test_exit_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 10)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)

    def test_entry_and_exit_sensors_detect_vehicle(self):
        # Since each test re-instantiates the classes, and since plate numbers are randomly generated,
        # I'm looking for the effect the detect_vehicle method in either class indirectly has on the
        # CarPark.available_bays property

        # Two cars come in:
        self.entry_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, 49)
        self.entry_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, 48)

        # Two cars leave:
        self.exit_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, 49)
        self.exit_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, 50)
