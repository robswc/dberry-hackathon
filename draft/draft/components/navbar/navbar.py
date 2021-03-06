import dash_html_components as html

# Navbar
navbar = html.Div([
    html.Div(
        className='navbar navbar-expand-lg navbar-light bg-light',
        children=[
            html.Div(
                className='container-fluid',
                children=[
                    html.Div('navbar-brand', 'dberry')
                ])
        ])
])