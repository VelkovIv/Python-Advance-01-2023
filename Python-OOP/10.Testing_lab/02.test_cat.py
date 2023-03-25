class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat('Blue')

    def test_size_increasing_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed, True)

    def test_cant_eat_if_fed_raiseing_error(self):
        self.cat.eat()
        with self.assertRaises(Exception) as expt:
            self.cat.eat()
        self.assertEqual(str(expt.exception), 'Already fed.')

    def test_cant_fall_a_asleep_if_not_fed_raise_error(self):
        with self.assertRaises(Exception) as expt:
            self.cat.sleep()
        self.assertEqual(str(expt.exception), 'Cannot sleep while hungry')

    def test_cant_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)

if __name__ == '__main__':
    unittest.main()
