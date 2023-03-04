from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.__budget -= price
        self.animals.append(animal)

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        needed_money = 0
        for worker in self.workers:
            needed_money += worker.salary

        if needed_money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_money

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        needed_money = 0

        for animal in self.animals:
            needed_money += animal.money_for_care

        if needed_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_money

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__create_status(self.animals, "Lion")
        result += self.__create_status(self.animals, "Tiger")
        result += self.__create_status(self.animals, "Cheetah")

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__create_status(self.workers, "Keeper")
        result += self.__create_status(self.workers, "Caretaker")
        result += self.__create_status(self.workers, "Vet")

        return result.strip()

    def __create_status(self, entities, entity_name):
        counter = 0
        result = ''
        for entity in entities:
            if entity.__class__.__name__ == entity_name:
                counter += 1
                result += repr(entity) + "\n"

        return f"----- {counter} {entity_name}s:\n" + result



