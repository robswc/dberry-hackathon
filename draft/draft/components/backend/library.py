import json

# import book
from components.backend.book import Book

class Shelf:
    def __init__(self):
        self.books = []


class Library:
    def __init__(self, title):
        self.title = title
        self.books = []
        self.shelves = []

    def create_shelf(self, title):
        pass

    def add_to_shelf(self, shelf):
        pass

    def remove_from_shelf(self, isbn):
        pass

    def add_book(self, book):
        self.books.append(book)

    def save_library(self):
        books = []
        for b in self.books:
            books.append({'title': b.title, 'authors': b.authors, 'rating': b.rating, 'description': b.description, 'img': b.img, 'isbn': b.isbn})
        lib = {'library': {'title': self.title, 'books': books}}
        with open('data/{}.txt'.format(self.title), 'w') as outfile:
            json.dump(lib, outfile)

    def load_library(self):
        with open('data/{}.txt'.format(self.title)) as json_file:
            data = json.load(json_file)
            for b in data.get('library').get('books'):
                book = Book()
                book.create_from_api(b.get('isbn'))
                self.books.append(book)
        pass