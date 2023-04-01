import unittest
from unittest import TestCase

from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_initialization(self):
        self.assertEqual(len(self.toy_store.toy_shelf), 7)
        for i in range(ord('A'), ord('G') + 1):
            self.assertIsNone(self.toy_store.toy_shelf[chr(i)])

    def test_add_toy_missing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('z', 'doll')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_toy_is_on_shelf(self):
        self.toy_store.toy_shelf['A'] = 'doll'
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'doll')
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_taken_shelf(self):
        self.toy_store.toy_shelf['A'] = 'car'
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'doll')
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_to_empty_shelf(self):
        res = self.toy_store.add_toy('A','car')
        self.assertEqual(res, "Toy:car placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf['A'], 'car')

    def test_remove_toy_not_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('Z', 'car')
        self.assertEqual(str(ex.exception),"Shelf doesn't exist!")

    def test_remove_toy_not_existing_toy(self):
        self.toy_store.toy_shelf['A'] = 'car'
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'doll')
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_existing_toy_from_existing_shelf(self):
        self.toy_store.toy_shelf['A'] = 'car'
        res = self.toy_store.remove_toy('A', 'car')
        self.assertEqual(res, "Remove toy:car successfully!")
        self.assertEqual(self.toy_store.toy_shelf['A'], None)



if __name__ == '__main':
    unittest.main()
