import unittest
from unittest import TestCase

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(10.5, 99.5)

    def test_class_variable(self):
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_initialization_values(self):
        self.assertEqual(self.vehicle.fuel, 10.5)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(self.vehicle.horse_power, 99.5)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_raise_exception(self):
        with self.assertRaises(Exception)  as ex:
            self.vehicle.drive(1000)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_fuel_reduce(self):
        self.vehicle.drive(2)
        self.assertEqual(self.vehicle.fuel, 8)

    def test_refuel_fuel_is_more_than_capaity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(40)
        self.assertEqual(str(ex.exception),"Too much fuel" )


    def test_refuel_fuel_is_less_than_capaity(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(2)
        self.assertEqual(self.vehicle.fuel, 2)

    def test__str__(self):
        self.assertEqual(self.vehicle.__str__(), "The vehicle has 99.5 horse power with " +
               "10.5 fuel left and 1.25 fuel consumption")

if __name__ == '__main':
    unittest.main()