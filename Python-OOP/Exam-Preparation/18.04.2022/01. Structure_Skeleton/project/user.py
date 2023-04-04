from typing import List
from project.movie_specification.movie import Movie


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List[Movie] = []
        self.movies_owned: List[Movie] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if value.strip() == '':
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        linked_movies = '\n'.join([m.details() for m in self.movies_liked])
        owned_movies = '\n'.join([m.details() for m in self.movies_owned])
        return f"Username: {self.username}, Age: {self.age}\n" \
               f"Liked movies:\n" \
               f"{linked_movies or 'No movies liked.'}\n" \
               f"Owned movies:\n" \
               f"{owned_movies or 'No movies owned.'}"


