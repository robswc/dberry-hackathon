import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Import app
from app import app

# Import pages
from pages.home import layout as home
from pages._import import layout as import_layout


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home
    elif pathname == '/import':
        return import_layout
    else:
        return home

if __name__ == '__main__':
    app.run_server(debug=True)