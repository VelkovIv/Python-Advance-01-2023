from typing import List, Dict

from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}  # dict: authors (key: str) his books (list of strings)
        self.rented_books: Dict[str: Dict[str: int]] = {}  # {usernames(str): {book names(str): days to return(int)}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:

        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}
            user.books.append(book_name)

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for info in self.rented_books.values():
            if book_name in info:
                return f'The book "{book_name}" is already rented and will be available in' \
                       f' {info[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> [str, None]:
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        if author not in self.books_available:
            self.books_available[author] = []

        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
