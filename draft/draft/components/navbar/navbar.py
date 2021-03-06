import dash_html_components as html

from app import app

# Navbar
navbar = html.Div([
    html.Div(
        className='navbar navbar-expand-lg navbar-light bg-light',
        children=[
            html.Div(
                className='container-fluid',
                children=[
                    html.Div(
                        children=html.Img(src=app.get_asset_url('img/white_text_logo.png'), style={'height': 50}),
                        className='navbar-brand'),
                    html.Div(
                        className='collapse navbar-collapse',
                        children=[
                            html.Ul(
                                className='navbar-nav',
                                children=[
                                    html.Li(html.A('Home', style={'color': 'white'}, className='nav-link')),
                                    html.Li(html.A('Import', style={'color': 'white'}, className='nav-link')),
                                    html.Li(html.A('Library', style={'color': 'white'}, className='nav-link')),
                                    html.Li(html.A('About', style={'color': 'white'}, className='nav-link')),
                                ]
                            )
                        ])
                ]
            ),
        ])
])