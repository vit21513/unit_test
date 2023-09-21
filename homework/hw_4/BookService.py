from abc import ABC, abstractmethod


class BookRepository(ABC):

    @abstractmethod
    def find_books_by_author(self, author):
        pass

    @abstractmethod
    def find_book_by_id(self, id):
        pass


class BookService:

    def __init__(self, book_repository:BookRepository):
        self.book_repository = book_repository

    def find_books_by_author(self, author):
        return self.book_repository.find_books_by_author(author)

    def find_book_by_id(self, id):
        return self.book_repository.find_book_by_id(id)
