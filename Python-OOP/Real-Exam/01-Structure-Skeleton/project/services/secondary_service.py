from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY: int = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        robots = [r.name for r in self.robots]
        return f"{self.name} Secondary Service:\n" \
               f"Robots: {' '.join(robots) or 'none'}"