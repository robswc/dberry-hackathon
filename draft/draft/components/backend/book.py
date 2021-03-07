import requests


class Book:
    def __init__(self, title='title', authors='author', isbn='111'):
        self.title = title
        self.authors = authors
        self.rating = 0
        self.isbn = isbn
        self.description = ''
        self.img = ''

    def create_from_api(self, isbn):
        url = 'https://www.googleapis.com/books/v1/volumes'
        params = {'q': 'isbn:{}'.format(isbn)}
        r = requests.get(url=url, params=params).json()
        book_data = r.get('items')[0].get('volumeInfo')
        self.title = book_data.get('title')
        self.authors = book_data.get('authors')
        self.rating = book_data.get('averageRating')
        self.isbn = isbn
        self.description = book_data.get('description')
        self.img = book_data.get('imageLinks').get('smallThumbnail')


    def __str__(self):
        return str('{} {} {}'.format(self.title, self.authors, self.isbn))


b = Book()
b.create_from_api('9780751565362')


print(b)
