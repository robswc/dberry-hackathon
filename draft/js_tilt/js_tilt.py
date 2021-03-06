import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from flask import send_from_directory

# #including tilt.js
external_scripts = [
    'https://cdnjs.cloudflare.com/ajax/libs/tilt.js/1.2.1/tilt.jquery.min.js',
    'https://unpkg.com/tilt.js@1.2.1/dest/tilt.jquery.min.js'
]

app = dash.Dash(__name__, external_scripts=external_scripts)

# app.head = [html.Link(rel='stylesheet', href='/assets/css/stylesheet.css')]

app.layout = html.Div([
    
    html.Div(
        className="app-header",
        children=[
            html.Div('d.berry tilt', className="app-header--title")
        ]
    ),

    html.Div([
        html.Div(
            children=html.Div([
                html.Div('''
                    I will make tilt work with Dash if it kills me
                ''')
            ])
        ),

        html.Div(
            html.Img(
                src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F4193iI6WHqL._SY344_BO1%2C204%2C203%2C200_.jpg&f=1&nofb=1"
            )
        )
    ])
])


@app.server.route("/assets/css")
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'assests')
    return send_from_directory(static_folder, path)

if __name__ == '__main__':
    app.run_server(debug=True)
