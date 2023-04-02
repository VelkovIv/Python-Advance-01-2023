from typing import List

from project.meals.meal import Meal


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill: float = 0.0
        self.ordered_meal_quantities = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if value[0:1] != '0' or len(value) != 10 or not value.isnumeric():
            raise ValueError("Invalid phone number!")

        self.__phone_number = value
