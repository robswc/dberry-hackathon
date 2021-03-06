import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State, MATCH, ALL
import dash
import json

# import app
from app import app
from components.backend.book import Book

# import libs
import requests


def render_search_book(title, authors, description, img, isbn):
    """
    Renders a book div
    :return:
    """
    print(img)
    print('isbn', isbn)
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
                            html.P('{}...'.format(' '.join(description.split(' ')[:5]))),
                            html.Button('Add to Library', className='add-button', id={'isbn': isbn})
                        ]
                    ),
                ]
            ),
        ]
    )

    return book_html


def render():
    img_upload = html.Div([
        dcc.Input(
            id='search-input',
            debounce=True,
            style={'width': '100%', 'font-weight': 'bolder', 'font-size': 'x-large'},
            placeholder='Search online for book...'),
        html.Div(id='search-output'),
        html.Div(id='search-output2')
    ])

    return img_upload

@app.callback(
    Output(component_id='search-output', component_property='children'),
    Input(component_id='search-input', component_property='value')
)
def search_book_api(input_value):

    # stop update if empty
    if input_value is None:
        print('prevent')
        raise PreventUpdate

    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {'q': input_value}
    r = requests.get(url, params=params).json()

    # put into book objects

    book_list = []
    for book in r.get('items'):
        vi = book.get('volumeInfo')
        title = vi.get('title')
        authors = vi.get('authors')
        isbn = vi.get('industryIdentifiers')[-1].get('identifier')
        if authors is None:
            authors = ['No authors provided']
        description = vi.get('description')
        if description is None:
            description = 'No description provided for this book.'
        if isbn is None:
            isbn = '101'
        try:
            img = vi.get('imageLinks').get('smallThumbnail')
        except:
            img = 'http://via.placeholder.com/80x100'

        book_list.append({'title': title,
                          'authors': authors,
                          'description': description,
                          'img': img,
                          'isbn': isbn
                          })



    rendered_books = []
    for b in book_list:
        html_div = render_search_book(b.get('title'), b.get('authors'), b.get('description'), b.get('img'), b.get('isbn'))
        rendered_books.append(html_div)

    returned = html.Div(
        className='',
        style={'height': '720px'},
        children=[
            html.Div('Results:', style={'padding-top': '1rem'}),
            html.Hr(),
            html.Div(
                className='scroll-wrapper',
                children=[
                    html.Ul(rendered_books, style={'padding': '0px'})
                ])
        ]
    )

    return returned

@app.callback(
    Output('search-output2', 'children'),
    Input({'isbn': ALL}, 'n_clicks')
)
def add_to_library(values):

    ctx = dash.callback_context
    print(ctx.triggered[0].get('prop_id'))
    print(type(ctx.triggered[0].get('prop_id')))


    return values