from project.band_members.musician import Musician


class Drummer(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.skills_to_learn = (
            "play the drums with drumsticks", "play the drums with drum brushes", "read sheet music")


