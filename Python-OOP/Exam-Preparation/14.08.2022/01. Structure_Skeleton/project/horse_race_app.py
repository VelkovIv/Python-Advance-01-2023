from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    @property
    def __get_house_types(self):
        return {
            "Appaloosa": Appaloosa,
            "Thoroughbred": Thoroughbred
        }

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = [h for h in self.horses if h.name == horse_name]
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.__get_house_types:
            horse = self.__get_house_types[horse_type](horse_name, horse_speed)
            self.horses.append(horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = self.get_jockey(jockey_name)
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def get_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.get_jockey(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self.find_free_horse(horse_type)
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def find_free_horse(self, horse_type):
        for horse in self.horses:
            if type(horse).__name__ == horse_type and not horse.is_taken:
                return horse

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        races_name = [r.race_type for r in self.horse_races]

        if race_type not in races_name:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.get_jockey(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        current_race = self.find_race(race_type)
        for race_jockey in current_race.jockeys:
            if race_jockey.name == jockey_name:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

        current_race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def find_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race

    def start_horse_race(self, race_type: str):
        races_name = [r.race_type for r in self.horse_races]

        if race_type not in races_name:
            raise Exception(f"Race {race_type} could not be found!")

        race = self.find_race(race_type)
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        jockey_name = ''
        horse_name = ''
        for jockey in race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                jockey_name = jockey.name
                horse_name = jockey.horse.name

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}! " \
               f"Winner's horse: {horse_name}."

