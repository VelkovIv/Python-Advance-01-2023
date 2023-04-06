from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name: str, oxygen: int = 90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= 15
