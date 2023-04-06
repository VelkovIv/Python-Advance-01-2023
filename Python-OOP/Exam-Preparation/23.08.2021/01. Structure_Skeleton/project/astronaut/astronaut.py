from abc import ABC, abstractmethod


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        ...

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
        return self.oxygen

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Oxygen: {self.oxygen}\n" \
               f"Backpack items: {', '.join(self.backpack) or 'none'}"
