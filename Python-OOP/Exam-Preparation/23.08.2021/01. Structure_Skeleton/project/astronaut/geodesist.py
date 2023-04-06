from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name: str, oxygen: int = 50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= 10

