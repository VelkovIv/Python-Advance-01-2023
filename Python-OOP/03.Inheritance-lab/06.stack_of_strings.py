class Stack:
    def __init__(self):
        self.data = []

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self) -> None:
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return "[" + f"{', '.join(self.data[i] for i in range(len(self.data)-1,-1,-1))}" + "]"
