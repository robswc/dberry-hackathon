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

    def render_book_full(self, title, authors, rating, description, img, isbn):
        """
        Renders a book div
        :return:
        """
        stars = []
        print('rating', rating)
        try:
            for i in range(0, round(rating)):
                stars.append('★')
        except:
            stars.append('')

        book_html = html.Div(
            className='card',
            children=[
                html.Div(
                    className='card-horizontal',
                    children=[
                        html.Div(
                            className='img-square-wrapper-full',
                            children=[
                                html.Img(
                                    src=img,
                                    style={'height': 180, 'width': 140, 'padding': '1rem'},
                                    className=''
                                )
                            ]
                        ),
                        html.Div(
                            className='card-body',
                            children=[
                                html.Div(title, className='card-title'),
                                html.Div(', '.join(authors), className='card-subtitle mb-2 text-muted'),
                                html.Div(''.join(stars), className='rating-stars'),
                                html.Div(
                                    className='description-container',
                                    children=[
                                        html.H4('Description'),
                                        html.P('{}...'.format(' '.join(description.split(' ')[:33]))),
                                    ]),

                            ]
                        ),
                    ]
                ),
            ]
        )

        return book_html

    def render_book(self, book, full):
        """
        Renders a book div
        :return:
        """

        if full is False:
            book_info = html.Div([
                html.Div(book.title, className='card-title-list'),
                html.Div(', '.join(book.authors), className='card-subtitle mb-2 text-muted')])
        else:
            book_info = html.Div([
                html.Div(book.title, className='card-title-list'),
                html.Div(', '.join(book.authors), className='card-subtitle mb-2 text-muted'),
                html.Div(book.description, className='text-muted')
            ])

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
                                    src=book.img,
                                    className='book-img'
                                )
                            ]
                        ),
                        html.Div(
                            className='card-body',
                            children=[
                                html.Div(book_info)
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
        for book in reversed(books):
            book_list.append(self.render_book(book, full=False))

        library = html.Div([
            html.Div(
                style={'padding-bottom': '1rem'},
                className='',
                children=[
                    dcc.Dropdown(
                        id='demo-dropdown',
                        options=[
                            {'label': 'default', 'value': 'default'},
                            {'label': 'rob', 'value': 'rob'},
                            {'label': 'user_001', 'value': 'user_001'},
                        ],
                        value='default',
                    ),
                ],
            ),
            html.Div(
                className='scroll-wrapper',
                children=[html.Ul(book_list, style={'padding': 0}, className='fade-in')]
            )
        ], id='library')

        return library

    def render_full(self, library):
        pass
        books = library.books
        book_list = []
        for b in reversed(books):
            print('Hereeee')
            book_list.append(
                html.Div(
                    className='flex-book',
                    children=[
                        self.render_book_full(b.title, b.authors, b.rating, b.description, b.img, b.isbn)
                    ]))

        library = html.Div([
            html.Div(
                style={'padding-bottom': '1rem'},
                className='',
                children=[
                    dcc.Dropdown(
                        id='demo-dropdown',
                        options=[
                            {'label': 'default', 'value': 'default'},
                            {'label': 'rob', 'value': 'rob'},
                            {'label': 'user_001', 'value': 'user_001'},
                        ],
                        value='default',
                    ),
                ],
            ),
            html.Div(
                className='scroll-wrapper',
                children=[html.Div(book_list, style={'padding': 0, 'display': 'flex', 'flex-wrap': 'wrap'}, className='fade-in')]
            )
        ], id='library')

        return library


# Main Library Interface
li = LibraryInterface()
