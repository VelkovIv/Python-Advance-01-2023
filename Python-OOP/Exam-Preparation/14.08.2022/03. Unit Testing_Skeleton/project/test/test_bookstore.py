import unittest
from unittest import TestCase

from project.bookstore import Bookstore

class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_initialization(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_initialization_books_limit_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -50
        self.assertEqual("Books limit of -50 is not valid", str(ve.exception))

    def test__len__total_number_of_books_in_bookstore(self):
        self.assertEqual(0, self.bookstore.__len__())
        self.bookstore.availability_in_store_by_book_titles = {"1":1,"2":2,"3":3,"4":4,"5":5}
        self.assertEqual(15, self.bookstore.__len__())

    def test_receive_books_more_books_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('just book', 20)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_books_enough_shelf_space(self):
        res = self.bookstore.receive_book('just book', 3)
        self.assertEqual("3 copies of just book are available in the bookstore.", res)
        self.assertEqual(3, self.bookstore.availability_in_store_by_book_titles['just book'])
        self.bookstore.receive_book('just book', 5)
        self.assertEqual(8, self.bookstore.availability_in_store_by_book_titles['just book'])

    def test_sell_book_not_available_book_raise_exception(self):
        self.bookstore.receive_book('just book', 5)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('just a book', 5)
        self.assertEqual("Book just a book doesn't exist!", str(ex.exception))

    def test_sell_book_not_enough_books_raise_exception(self):
        self.bookstore.receive_book('just book', 3)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('just book', 5)
        self.assertEqual("just book has not enough copies to sell. Left: 3", str(ex.exception))

    def test_sell_book(self):
        self.bookstore.receive_book('just book', 5)
        res = self.bookstore.sell_book('just book', 5)
        self.assertEqual("Sold 5 copies of just book", res)
        self.assertEqual({'just book': 0}, self.bookstore.availability_in_store_by_book_titles)

    def test__str__(self):
        self.bookstore.receive_book('just book', 5)
        self.bookstore.sell_book('just book', 3)
        res = 'Total sold books: 3\n' + 'Current availability: 2\n' + ' - just book: 2 copies'
        self.assertEqual(res, self.bookstore.__str__())




if __name__ =='__main__':
    unittest.main()