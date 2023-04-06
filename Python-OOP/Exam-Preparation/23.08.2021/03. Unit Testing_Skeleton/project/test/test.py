import unittest
from unittest import TestCase

from project.library import Library


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library('Library')

    def test_init_library(self):
        self.assertEqual('Library', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_init_library_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book(self):
        self.library.add_book('author', 'book')
        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertEqual(['book'], self.library.books_by_authors['author'])

    def test_add_reader(self):
        self.library.add_reader('Ivan')
        self.assertEqual([], self.library.readers['Ivan'])
        res = self.library.add_reader('Ivan')
        self.assertEqual(res, "Ivan is already registered in the Library library.")

    def test_rent_book_no_reader(self):
        res = self.library.rent_book('Ivan','author', 'book')
        self.assertEqual(res, "Ivan is not registered in the Library Library.")


    def test_rent_book_no_author(self):
        self.library.add_reader('Ivan')
        res = self.library.rent_book('Ivan', 'author', 'book')
        self.assertEqual(res, "Library Library does not have any author's books.")

    def test_rent_book_no_book(self):
        self.library.add_reader('Ivan')
        self.library.add_book('author', 'Book')
        res = self.library.rent_book('Ivan', 'author', 'book')
        self.assertEqual(res, """Library Library does not have author's "book".""")

    def test_rent_book_(self):
        self.library.add_reader('Ivan')
        self.library.add_book('author', 'book')
        self.library.add_book('author', 'Book')
        self.library.rent_book('Ivan', 'author', 'book')
        self.assertEqual([{'author':'book'}], self.library.readers['Ivan'])
        self.assertEqual(['Book'], self.library.books_by_authors['author'])




if __name__ == '__main__':
    unittest.main()
