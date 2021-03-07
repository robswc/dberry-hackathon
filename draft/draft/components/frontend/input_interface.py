import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State, MATCH, ALL
import dash
import json
import time
import tkinter

# import app
from app import app
from components.backend.book import Book
from components.frontend.library_interface import li

# import libs
import requests


def render_search_book(title, authors, rating, description, img, isbn):
    """
    Renders a book div
    :return:
    """
    stars = []
    print('rating', rating)
    for i in range(0, round(rating)):
        stars.append('★')


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
                            html.Button('Add to Library', className='add-button', id={'isbn': isbn}),

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
            autoComplete='off',
            debounce=True,
            style={'width': '100%', 'font-weight': 'bolder', 'font-size': 'x-large'},
            placeholder='Search online for book...'),
        html.Div(id='search-output'),
        html.Div(id='search-output2'),
    ])

    return img_upload


@app.callback(
    [Output(component_id='search-output', component_property='children')],
    [Input(component_id='search-input', component_property='value'),
     Input({'ocr-add': ALL}, 'n_clicks')]
)
def search_book_api(input_value, ocr_add):
    # stop update if empty
    ctx = dash.callback_context
    print('searching books...')
    if input_value is None and ctx.triggered[0].get('value') is None:
        print(ctx.triggered[0])
        print('Preventing update')
        raise PreventUpdate


    print(ctx.triggered[0])
    if ctx.triggered[0].get('prop_id') != 'search-input.value' and ctx.triggered[0].get('prop_id') != '.':
        if ctx.triggered[0].get('value') is not None:
            if int(ctx.triggered[0].get('value')) > 0:
                input_value = json.loads(ctx.triggered[0].get('prop_id').split('.n_clicks')[0]).get('ocr-add')


    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {'q': input_value}

    r = requests.get(url, params=params).json()

    print('ip', input_value)
    print(r)

    # put into book objects

    book_list = []
    for book in r.get('items'):
        vi = book.get('volumeInfo')
        title = vi.get('title')
        authors = vi.get('authors')
        rating = vi.get('averageRating')
        isbn = vi.get('industryIdentifiers')[-1].get('identifier')
        if authors is None:
            authors = ['No authors provided']
        if rating is None:
            rating = 0
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
                          'rating': rating,
                          'description': description,
                          'img': img,
                          'isbn': isbn
                          })

    rendered_books = []
    for b in book_list:
        html_div = render_search_book(b.get('title'), b.get('authors'), b.get('rating'), b.get('description'), b.get('img'),
                                      b.get('isbn'))
        rendered_books.append(html.Li(html_div))

    returned = html.Div(
        className='',
        style={'height': '820px'},
        children=[
            html.Div('Results:', style={'padding-top': '1rem'}),
            html.Hr(),
            html.Div(
                className='scroll-wrapper',
                children=[
                    html.Ul(rendered_books, style={'padding': '0px'}, className='fade-in'),
                ])
        ]
    )

    return [returned]


@app.callback(
    Output('search-output2', 'children'),
    Input({'isbn': ALL}, 'n_clicks')
)
def add_to_library(values):
    ctx = dash.callback_context
    if ctx.triggered[0].get('value') == 1:
        isbn = json.loads(ctx.triggered[0].get('prop_id').split('.n_clicks')[0]).get('isbn')
        b = Book()
        b.create_from_api(isbn)
        li.get_library('default').add_book(b)

    return values


@app.callback(
    Output('library', 'children'),
    Input({'isbn': ALL}, 'n_clicks')
)
def adds(values):
    time.sleep(0.5)
    li.get_library('default').save_library()
    return li.render(li.get_library('default'))
