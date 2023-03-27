import unittest
from unittest import TestCase

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Test animal','just name', 'just sound')

    def test_initialization_of_mammal(self):
        self.assertEqual(self.mammal.name,'Test animal')
        self.assertEqual(self.mammal.type,'just name')
        self.assertEqual(self.mammal.sound,'just sound')

    def test_mammal_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual(result, "Test animal makes just sound")

    def test_get_kingdom_result(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.mammal.info(), "Test animal is of type just name")


if __name__ == '__main__':
    unittest.main()