from CarManager.car_manager import Car
import unittest


class CarTest(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car('myCar', 'Audi', 5, 80)

    def test_constructor(self):
        self.assertEqual(self.car.make, 'myCar')
        self.assertEqual(self.car.model, 'Audi')
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 80)

    def test_constructor_make_raise_error(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ''
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_constructor_model_raise_error(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ''
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_constructor_fuel_consumption_is_zero_or_negative_raise_errors(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -5
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_constructor_fuel_capacity_is_zero_or_negative_raise_errors(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -5
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_constructor_fuel_amound_is_negative_raise_error(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -5
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_constructor_fuel_amound_is_positive(self):
        result = self.car.fuel_amount = 6
        self.assertEqual(result, 6)

    def test_refuels_zero_or_negative_raise_errors(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")
        with self.assertRaises(Exception) as context:
            self.car.refuel(-6)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_bigger_then_cappasity(self):
        self.car.refuel(90)
        self.assertEqual(self.car.fuel_amount, 80)

    def test_refuel_lower_then_cappasity(self):
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_amount, 50)

    def test_drive(self):
        self.car.refuel(70)
        self.car.drive(200)
        self.assertEqual(self.car.fuel_amount, 60)

    def test_drive_raise_error(self):
        self.car.refuel(8)
        with self.assertRaises(Exception) as context:
            self.car.drive(200)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
