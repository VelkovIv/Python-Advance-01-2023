from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    @property
    def get_delicacy(self):
        return {
            'Gingerbread': Gingerbread,
            'Stolen': Stolen
        }

    @property
    def get_booth(self):
        return {
            'Open Booth': OpenBooth,
            'Private Booth': PrivateBooth
        }

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        delicacy_names = [d.name for d in self.delicacies]
        if name in delicacy_names:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.get_delicacy:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.get_delicacy[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
        booth_numbers = [b.booth_number for b in self.booths]
        if booth_number in booth_numbers:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.get_booth:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.get_booth[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str:
        free_booths = [b for b in self.booths if not b.is_reserved]
        for booth in free_booths:
            if booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        # booth = [b for b in self.booths if b.booth_number == booth_number][0]
        # if not booth:
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        # delicacy = [d for d in self.delicacies if d.name == delicacy_name][0]
        # if not delicacy:
        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:

            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int) -> str:
        booth = [b for b in self.booths if b.booth_number == booth_number][0]

        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill
        booth.is_reserved = False
        booth.price_for_reservation = 0
        booth.delicacy_orders = []

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self) -> str:
        return f"Income: {self.income:.2f}lv."
