from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def food_to_eat(self):
        return [Meat]

    @property
    def specific_weight(self):
        return 0.25


class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def food_to_eat(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def specific_weight(self):
        return 0.35
