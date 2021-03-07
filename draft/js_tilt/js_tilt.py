import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from flask import send_from_directory
import os

assets_path = os.getcwd() +'/assets'
app = dash.Dash(__name__, assets_folder=assets_path)

app.layout = html.Div([
    
    html.Div(
        className="box",
    ),
   
])


@app.server.route("/assets/css")
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'assests')
    return send_from_directory(static_folder, path)

if __name__ == '__main__':
    app.run_server(debug=True)
