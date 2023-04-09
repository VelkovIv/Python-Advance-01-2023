from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    @property
    def __valid_service_types(self):
        return {
            "MainService": MainService,
            "SecondaryService": SecondaryService
        }

    @property
    def __valid_robot_types(self):
        return {
            "MaleRobot": MaleRobot,
            "FemaleRobot": FemaleRobot
        }

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in self.__valid_service_types:
            raise Exception("Invalid service type!")

        service = self.__valid_service_types[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        if robot_type not in self.__valid_robot_types:
            raise Exception("Invalid robot type!")

        robot = self.__valid_robot_types[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = self.__find_robot(robot_name)
        service = self.__find_service(service_name)
        if robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService" or \
                robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService":
            return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = self.__find_service(service_name)

        for robot in service.robots:
            if robot.name == robot_name:
                service.robots.remove(robot)
                self.robots.append(robot)

                return f"Successfully removed {robot_name} from {service_name}."

        raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self.__find_service(service_name)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service(service_name)

        total_price = 0
        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = ''
        for service in self.services:
            result += service.details() + '\n'
        return result.rstrip()

    def __find_robot(self, name: str):
        for robot in self.robots:
            if robot.name == name:
                return robot

    def __find_service(self, name: str):
        for service in self.services:
            if service.name == name:
                return service
