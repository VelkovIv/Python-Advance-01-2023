import unittest
from unittest import TestCase

from project.movie import Movie

class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Just Movie", 2020, 6.7)

    def test_initialization(self):
        self.assertEqual(self.movie.name, "Just Movie")
        self.assertEqual(self.movie.year, 2020)
        self.assertEqual(self.movie.rating, 6.7)
        self.assertEqual(self.movie.actors, [])

    def test_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_year_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1800
        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor(self):
        self.movie.add_actor('Actor1')
        self.assertEqual(len(self.movie.actors), 1)
        self.assertEqual(self.movie.actors[0], "Actor1")
        res = self.movie.add_actor('Actor1')
        self.assertEqual(res, "Actor1 is already added in the list of actors!")
        self.movie.add_actor('Actor2')
        self.assertEqual(self.movie.actors[1], "Actor2")
        self.assertEqual(len(self.movie.actors), 2)

    def test__gt__(self):
        movie1 = Movie("Movie", 2019, 5.4)
        res = '"Just Movie" is better than "Movie"'
        self.assertEqual(self.movie.__gt__(movie1), res)
        movie2 = Movie("Movie", 2019, 9.4)
        res1 = '"Movie" is better than "Just Movie"'
        self.assertEqual(self.movie.__gt__(movie2), res1)

    def test__repr__(self):
        self.movie.add_actor('Actor1')
        self.movie.add_actor('Actor2')
        result = 'Name: Just Movie\nYear of Release: 2020\nRating: 6.70\nCast: Actor1, Actor2'
        self.assertEqual(self.movie.__repr__(), result)


if __name__ =='__main__':
    unittest.main()
