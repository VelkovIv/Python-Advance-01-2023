from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_mission = 0
        self.not_successful_mission = 0

    @property
    def get_astronaut_type(self):
        return {
            "Biologist": Biologist,
            "Geodesist": Geodesist,
            "Meteorologist": Meteorologist
        }

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type not in self.get_astronaut_type:
            raise Exception("Astronaut type is not valid!")

        astronaut = self.get_astronaut_type[astronaut_type](name)
        self.astronaut_repository.add(astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name)
        self.planet_repository.add(planet)
        planet.items = items.split(', ')

        return f"Successfully added Planet: {planet.name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def find_astronauts_with_oxygen_above_30(self):
        astronauts = []
        for astronaut in sorted(self.astronaut_repository.astronauts, key=lambda a: -a.oxygen):
            if astronaut.oxygen >= 30:
                astronauts.append(astronaut)
            if len(astronauts) == 5:
                break

        return astronauts

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        astronauts_for_mission = self.find_astronauts_with_oxygen_above_30()
        if not astronauts_for_mission:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts = 0
        for astronaut in sorted(astronauts_for_mission, key=lambda a: -a.oxygen):
            astronauts += 1
            while astronaut.oxygen > 0 and planet.items == 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

            if len(planet.items) == 0:
                self.successful_mission += 1
                return f"Planet: {planet_name} was explored. {astronauts} astronauts participated in collecting items."

        self.not_successful_mission += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.successful_mission} successful missions!\n" \
                 f"{self.not_successful_mission} missions were not completed!\nAstronauts' info:\n"

        result += '\n'.join(str(a) for a in self.astronaut_repository.astronauts) + "\n"

        return result.rstrip('\n')
