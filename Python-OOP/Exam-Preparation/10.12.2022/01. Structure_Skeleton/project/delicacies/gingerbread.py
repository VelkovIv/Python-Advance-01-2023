from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION: int = 200

    def __init__(self, name: str, price: float,):
        super().__init__(name, self.PORTION, price)

    def details(self):
        return f"Gingerbread {self.name}: {self.PORTION}g - {self.price:.2f}lv."



