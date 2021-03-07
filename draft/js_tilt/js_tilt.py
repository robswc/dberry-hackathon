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
    
    # html.Div(
    #     className="app-header",
    #     children=[
    #         html.Div('d.berry Tilt.js', className="app-header--title")
    #     ]
    # ),

    # html.Div([
    #     html.Div(
    #         children=html.Div([
    #             html.Div('''
    #                 I will make tilt work with Dash if it kills me
    #             ''')
    #         ])
    #     )
    # ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
