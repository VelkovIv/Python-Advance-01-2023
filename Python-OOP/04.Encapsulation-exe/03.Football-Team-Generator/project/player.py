class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        return f"Player: {self.name}\n" + \
               f"Sprint: {self.__sprint}\n" + \
               f"Dribble: {self.__dribble}\n" + \
               f"Passing: {self.__passing}\n" + \
               f"Shooting: {self.__shooting}"

