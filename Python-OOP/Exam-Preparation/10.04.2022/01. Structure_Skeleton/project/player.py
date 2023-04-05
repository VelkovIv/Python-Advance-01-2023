from project.supply.supply import Supply


class Player:
    PLAYER_NAMES = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.need_sustenance: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError("Name not valid!")
        if value in Player.PLAYER_NAMES:
            raise Exception(f"Name {value} is already used!")
        Player.PLAYER_NAMES.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value: int):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        if self.stamina == 100:
            self.need_sustenance = False
        else:
            self.need_sustenance = True
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
