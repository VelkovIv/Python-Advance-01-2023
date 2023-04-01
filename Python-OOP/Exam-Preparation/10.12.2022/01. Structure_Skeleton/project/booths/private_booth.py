from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON: float = 3.5

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.PRICE_PER_PERSON
        self.is_reserved = True
