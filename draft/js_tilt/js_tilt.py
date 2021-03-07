import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from flask import send_from_directory
import os


app = dash.Dash(__name__)

app.layout = html.Div([

    html.Section(children=[
        html.Div(className='box tilt')
    ])
    
    html.Div(
        className="box",
    ),
   
])


if __name__ == '__main__':
    app.run_server(debug=True)
