from abc import ABC, abstractmethod
import math


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: [str, None] = None
        self.ram: [int, None] = None
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def computer_type(self):
        ...

    @property
    @abstractmethod
    def available_processors(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    def configure_computer(self, processor: str, ram: int) -> str:
        if processor not in self.available_processors:
            raise ValueError(
                f"{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        if not self.valid_ram(ram) or ram > self.max_ram:
            raise ValueError(
                f"{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.price += self.available_processors[processor]
        self.ram = ram
        self.price += int(math.log2(ram)) * 100

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

    @staticmethod
    def valid_ram(ram: int):
        ram_size = math.log2(ram)
        return math.ceil(ram_size) == math.floor(ram_size)

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
