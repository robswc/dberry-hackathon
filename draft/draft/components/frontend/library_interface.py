import dash_html_components as html
import dash_core_components as dcc

# import library
from components.backend.library import Library


class LibraryInterface:
    def __init__(self):
        self.libraries = []

    def create_library(self, title):
        self.libraries.append(Library(title))

    def get_library(self, title):
        for lib in self.libraries:
            if lib.title == title:
                return lib

    def render_book(self, book):
        """
        Renders a book div
        :return:
        """
        book_html = html.Div(
            className='card',
            children=[
                html.Div(
                    className='card-horizontal',
                    children=[
                        html.Div(
                            className='img-square-wrapper',
                            children=[
                                html.Img(
                                    src='http://via.placeholder.com/80x100',
                                    className=''
                                )
                            ]
                        ),
                        html.Div(
                            className='card-body',
                            children=[
                                html.Div(book.title, className='card-title'),
                                html.Div(book.author, className='card-subtitle mb-2 text-muted'),
                            ]
                        ),
                    ]
                ),
            ]
        )

        return book_html

    def render(self, library):



        books = library.books
        book_list = []
        for book in books:
            print('Hereeee')
            book_list.append(self.render_book(book))

        library = html.Div([
            html.Div(
                style={'padding-bottom': '1rem'},
                className='',
                children=[
                    dcc.Dropdown(
                        id='demo-dropdown',
                        options=[
                            {'label': 'default', 'value': 'default'},
                        ],
                        value='default',
                    ),
                ],
            ),
            html.Div(
                className='scroll-wrapper',
                children=[html.Ul(book_list, style={'padding': 0})]
            )
        ])

        return library


# Main Library Interface
li = LibraryInterface()
