class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Petar Petrov", 2000, 1)
        self.assertEqual(self.worker.name, "Petar Petrov")
        self.assertEqual(self.worker.salary, 2000)
        self.assertEqual(self.worker.energy, 1)

    def test_resting(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 2)

    def test_work_with_zero_or_negative_energy(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 0)
        with self.assertRaises(Exception) as message:
            self.worker.work()
        self.assertEqual(str(message.exception), 'Not enough energy.')

    def test_salary_increasing(self):
        worker = Worker("Petar Petrov", 2000, 5)
        worker.work()
        self.assertEqual(worker.salary, 2000)

    def test_energy_decresing_after_working(self):
        worker = Worker("Petar Petrov", 2000, 5)
        worker.work()
        self.assertEqual(worker.energy, 4)

    def test_get_info(self):
        worker = Worker("Petar Petrov", 2000, 5)
        result = f'Petar Petrov has saved 0 money.'
        self.assertEqual(worker.get_info(), result)
        worker.work()
        result = f'Petar Petrov has saved 2000 money.'
        self.assertEqual(worker.get_info(), result)


if __name__ == "__main__":
    unittest.main()
