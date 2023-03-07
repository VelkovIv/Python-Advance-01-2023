class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

        __class__.id += 1

    @staticmethod
    def get_next_id():
        return Equipment.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
