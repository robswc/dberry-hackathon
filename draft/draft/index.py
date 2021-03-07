import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import time

# Import app
from app import app

# Import pages
from pages.home import layout as home
from pages._import import layout as import_layout
from pages.library import layout as library_layout
from pages.about import layout as about_layout


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return about_layout
    elif pathname == '/import':
        return import_layout
    elif pathname == '/library':
        return library_layout
    elif pathname == '/about':
        return about_layout
    else:
        return about_layout


if __name__ == '__main__':
    app.run_server(debug=True)