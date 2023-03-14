from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.foot_eaten = 0

    @property
    @abstractmethod
    def food_to_eat(self):
        ...

    @property
    @abstractmethod
    def specific_weight(self):
        ...


    @staticmethod
    @abstractmethod
    def make_sound():
        ...

    def feed(self, food):
        if type(food) not in self.food_to_eat:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.specific_weight
        self.foot_eaten += food.quantity


class Bird(Animal, ABC):

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.foot_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.foot_eaten}]"
