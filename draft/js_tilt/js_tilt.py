import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from flask import send_from_directory

app.head = [html.Link(rel='stylesheet', href='/assets/css/stylesheet.css')]

app.layout = html.Div([
])


@app.server.route("/assets/css")
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'assests')
    return send_from_directory(static_folder, path)

if __name__ == '__main__':
    app.run_server(debug=True)