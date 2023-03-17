class vowels:
    def __init__(self, iterable):
        self.vowels = ['a', 'o', 'y', 'e', 'i', 'u']
        self.iterable = [el for el in iterable if el.lower() in self.vowels]
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx - 1 < len(self.iterable):
            if self.iterable[self.idx - 1].lower() in self.vowels:
                return self.iterable[self.idx - 1]

        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
