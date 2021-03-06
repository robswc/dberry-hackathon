import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    ),
    
    html.Img(
        src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.FSEs7JbMmmOvXa8UFA9a2QAAAA%26pid%3DApi&f=1"
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)