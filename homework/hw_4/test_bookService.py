import unittest
from unittest.mock import Mock
from BookService import BookService


class TestBookService(unittest.TestCase):

    def setUp(self) -> None:
        self.book_repository = Mock()
        self.author = "Лев Толстой"
        self.list_books = [Mock(title="Анна Каренина"), Mock(title="Детство")]

    def test_find_books_by_author(self):
        self.book_repository.find_books_by_author.return_value = self.list_books
        book_service = BookService(self.book_repository)
        sort_books = book_service.find_books_by_author(self.author)
        self.assertEqual(self.list_books, sort_books)

    def test_find_book_by_id(self):
        book_repository = Mock()
        book_id = 1
        expected_book = Mock(title="Азбука")
        book_repository.find_book_by_id.return_value = expected_book
        book_service = BookService(book_repository)
        book = book_service.find_book_by_id(book_id)
        self.assertEqual(expected_book, book)
