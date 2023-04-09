import unittest

from project.tennis_player import TennisPlayer


class TestTennisPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer('Grigor', 35, 1000.56)

    def test_initialization(self):
        self.assertEqual(self.player.name, 'Grigor')
        self.assertEqual(self.player.age, 35)
        self.assertEqual(self.player.points, 1000.56)
        self.assertEqual(self.player.wins, [])

    def test_name_initialization_raise_value_error_shorten_name(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Gr'
        self.assertEqual(str(ve.exception), 'Name should be more than 2 symbols!')

    def test_age_initialization_raise_value_error_lower_age(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        self.assertEqual(str(ve.exception), 'Players must be at least 18 years of age!')

    def test_add_new_win(self):
        self.player.add_new_win('Sofia Open')
        self.assertEqual(self.player.wins, ['Sofia Open'])
        res = self.player.add_new_win('Sofia Open')
        self.assertEqual(res, 'Sofia Open has been already added to the list of wins!')

    def test__lt__(self):
        other = TennisPlayer('Beker', 35, 870.10)
        res = self.player.__lt__(other)
        self.assertEqual(res,'Grigor is a better player than Beker')
        other.points = 1100
        res1 = self.player.__lt__(other)
        self.assertEqual(res1,'Beker is a top seeded player and he/she is better than Grigor')

    def test__str__(self):
        self.player.add_new_win('Sofia Open')
        self.player.add_new_win('Plovdiv Open')
        res = self.player.__str__()
        expected = 'Tennis Player: Grigor\nAge: 35\nPoints: 1000.6\nTournaments won: Sofia Open, Plovdiv Open'
        self.assertEqual(res, expected)




if __name__ == '__main__':
    unittest.main()
