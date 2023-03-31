from project.band_members.musician import Musician


class Guitarist(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.skills_to_learn =("play metal", "play rock", "play jazz")


