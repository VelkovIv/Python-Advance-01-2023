from typing import List
from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    @property
    def valid_car_types(self):
        return {
            "MuscleCar": MuscleCar,
            "SportsCar": SportsCar
        }

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = self.__find_car_by_model(model)
        if car:
            raise Exception(f"Car {model} is already created!")

        car = self.valid_car_types[car_type](model, speed_limit)
        self.cars.append(car)

        return f"{car_type} {model} is created."

    def __find_car_by_model(self, model):
        for car in self.cars:
            if car.model == model:
                return car

    def create_driver(self, driver_name: str):
        driver = self.__find_driver(driver_name)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)

        return f"Driver {driver_name} is created."

    def __find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def create_race(self, race_name: str):
        race = self.__find_race(race_name)
        if race:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)

        return f"Race {race_name} is created."

    def __find_driver(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver

    def __find_car_for_driver(self, model):
        for i in range(len(self.cars) - 1, -1, -1):
            if type(self.cars[i]).__name__ == "MuscleCar" and not self.cars[i].is_taken:
                return self.cars[i]
            elif type(self.cars[i]).__name__ == "SportsCar" and not self.cars[i].is_taken:
                return self.cars[i]

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_car_for_driver(car_type)
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            driver.car.is_taken = False
            old_model = driver.car.model
            driver.car = car
            new_model = driver.car.model
            car.is_taken = True

            return f"Driver {driver.name} changed his car from {old_model} to {new_model}."

        driver.car = car
        car.is_taken = True

        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__find_driver(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = ''
        top_three_winners = 0
        for driver in sorted(race.drivers, key=lambda d: -d.car.speed_limit):
            top_three_winners += 1
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"
            driver.number_of_wins += 1
            if top_three_winners == 3:
                return result.rstrip('\n')
