from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY: int = 30

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        robots = [r.name for r in self.robots]
        return f"{self.name} Main Service:\n" \
               f"Robots: {' '.join(robots) or 'none'}"

