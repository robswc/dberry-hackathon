import dash_html_components as html
import dash_core_components as dcc


def render_book(book):
    """
    Renders a book div
    :return:
    """
    html.Div()

def render(library):
    books = library.books

    book_list = []
    for book in books:
        book_list.append(render_book(book))


    library = html.Div([
        html.Ul(book_list)
    ])

    return library
