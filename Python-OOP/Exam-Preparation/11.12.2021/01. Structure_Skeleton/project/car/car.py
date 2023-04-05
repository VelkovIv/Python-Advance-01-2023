from abc import ABC, abstractmethod


class Car(ABC):
    MINIMUM_SPEED_LIMIT = 0
    MAXIMUM_SPEED_LIMIT = 0

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value < self.MINIMUM_SPEED_LIMIT or value > self.MAXIMUM_SPEED_LIMIT:
            raise ValueError(f"Invalid speed limit! Must be between {self.MINIMUM_SPEED_LIMIT} and "
                             f"{self.MAXIMUM_SPEED_LIMIT}!")
        self.__speed_limit = value
