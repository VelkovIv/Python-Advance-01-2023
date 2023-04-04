from typing import List
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        user = self.__find_user(username)
        if user:
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)

        return f"{username} registered successfully."

    def __find_user(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def __movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if not user:
            raise Exception("This user does not exist!")

        # current_movie = [m for m in user.movies_owned if m == movie]
        if not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if self.__movie_exists(movie.title):
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.__movie_exists(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = self.__find_user(username)
        if movie.owner == user:
            for el, value in kwargs.items():
                setattr(movie, el, value)

            return f"{username} successfully edited {movie.title} movie."

        raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    def delete_movie(self, username: str, movie: Movie):
        if not self.__movie_exists(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = self.__find_user(username)
        if movie.owner == user:
            self.movies_collection.remove(movie)
            user.movies_owned.remove(movie)

            return f"{username} successfully deleted {movie.title} movie."

        raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if user.movies_liked == movie:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1

        return f"{username} liked {movie.title} movie."

    def __user_like_movie(self, username: str, movie_title: str):
        user = self.__find_user(username)
        for movie in user.movies_liked:
            if movie.title == movie_title:
                return True
            return False

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if not [m for m in user.movies_liked if
                m.title == movie.title]:  # self.__user_like_movie(username, movie.title):
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."
        result = []
        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            result.append(movie.details())

        return '\n'.join(result)

    def __str__(self):
        all_users = ', '.join([u.username for u in self.users_collection])
        all_movies = ', '.join([m.title for m in self.movies_collection])
        return f"All users: {all_users or 'No users'}\nAll movies: {all_movies or 'No movies'}"
