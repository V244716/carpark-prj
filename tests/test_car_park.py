import unittest
from pathlib import Path
from car_park import CarPark
import json

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)

    def test_car_park_initialised_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))
        self.assertEqual(self.car_park.config_file, Path("config.json"))

    def tearDown_all(self):
        Path("config.json").unlink(missing_ok=True)
        Path("log.txt").unlink(missing_ok=True)

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

        self.tearDown_all()

    def test_remove_car(self):
        self.car_park.add_car("FAKE-002")
        self.car_park.remove_car("FAKE-002")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

        self.tearDown_all()

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FULL-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FULL-111")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FULL-111")
        self.assertEqual(self.car_park.available_bays, 0)

        self.tearDown_all()

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

        self.tearDown_all()

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

        self.tearDown_all()

    def test_log_file_created(self):
        new_carpark = CarPark("123 Example Street", 100, log_file = "new_log.txt")
        self.assertTrue(Path("new_log.txt").exists())

        self.tearDown_all()
    def tearDown(self):
        Path('new_log.txt').unlink(missing_ok=True)

    def test_car_logged_when_entering(self):
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open("r") as file:
            last_line = file.readlines()[-1]
        self.assertIn("NEW-001", last_line) # check plate entered
        self.assertIn("entered", last_line) # check description
        self.assertIn("\n", last_line,) # check entry has a new line

        self.tearDown_all()

    def test_car_logged_when_exiting(self):
        self.car_park.add_car("EXIT-001")
        self.car_park.remove_car("EXIT-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("EXIT-001", last_line) # check plate entered
        self.assertIn("exited", last_line) # check description
        self.assertIn("\n", last_line,) # check entry has a new line

        self.tearDown_all()

    def test_config_file_created(self):
        new_carpark = CarPark("123 Example Street", 100, config_file="new_config.json")
        self.assertTrue(Path("new_config.json").exists())
        Path("new_config.json").unlink()

    def test_config_file_written(self):
        self.car_park.write_config()
        with self.car_park.config_file.open("r") as file:
            cp = json.load(file)
        self.assertEqual(cp, {'location':'123 Example Street', 'capacity':100, 'log_file':'log.txt'})

        self.tearDown_all()

    def test_CarPark_initialised_from_config_file(self):
        new_carpark = CarPark("456 Saved Street", 200)
        new_carpark.write_config()
        next_new_carpark = CarPark.from_config()
        self.assertEqual("456 Saved Street", next_new_carpark.location)
        self.assertEqual(200, next_new_carpark.capacity)

        self.tearDown_all()



if __name__ == "__main__":
    unittest.main()


