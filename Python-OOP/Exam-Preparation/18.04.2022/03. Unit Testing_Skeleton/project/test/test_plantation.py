import unittest
from unittest import TestCase

from project.plantation import Plantation


class TestPlantation(TestCase):

    def setUp(self):
        self.plantation = Plantation(100)

    def test_initialization_attributes(self):
        self.assertEqual(self.plantation.size, 100)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_size_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -5
        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker(self):
        res = self.plantation.hire_worker('worker')
        self.assertEqual(res, "worker successfully hired.")
        self.assertEqual(len(self.plantation.workers), 1)
        self.assertEqual(self.plantation.workers[0], 'worker')

    def test_hire_worker_raise_value_error(self):
        self.plantation.hire_worker('worker')
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('worker')
        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test__len__(self):
        self.plantation.hire_worker('worker')
        self.plantation.planting('worker', 'rose')
        self.assertEqual(self.plantation.__len__(), 1)

    def test_planting_(self):
        self.plantation.hire_worker('worker')
        res = self.plantation.planting('worker', 'rose')
        self.assertEqual(res, "worker planted it's first rose.")
        self.assertEqual(len(self.plantation.plants), 1)
        self.assertEqual(self.plantation.plants['worker'], ['rose'])
        res = self.plantation.planting('worker', 'tulip')
        self.assertEqual(self.plantation.plants['worker'], ['rose', 'tulip'])
        self.assertEqual(len(self.plantation.plants['worker']),2)
        self.assertEqual(res, "worker planted tulip.")

    def test_planting_raise_value_error_worker(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('worker', 'rose')
        self.assertEqual(str(ve.exception), "Worker with name worker is not hired!")

    def test_planting_raise_value_error_plantation_is_full(self):
        self.plantation.size = 1
        self.plantation.hire_worker('worker')
        self.plantation.planting('worker', 'rose')
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('worker', 'tulip')
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test__str__(self):
        self.plantation.hire_worker('worker')
        self.plantation.planting('worker', 'rose')
        self.plantation.planting('worker', 'tulip')
        result = 'Plantation size: 100\nworker\nworker planted: rose, tulip'
        self.assertEqual(self.plantation.__str__(), result)

    def test__repr__(self):
        self.plantation.hire_worker('worker')
        self.plantation.planting('worker', 'rose')
        self.plantation.planting('worker', 'tulip')
        result = 'Size: 100\nWorkers: worker'
        self.assertEqual(self.plantation.__repr__(), result)


if __name__ == '__main__':
    unittest.main()
