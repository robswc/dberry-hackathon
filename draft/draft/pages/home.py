import dash_html_components as html

# Navbar
from components.navbar import navbar

# Components
from components.frontend import renders

tiles = [
    renders.render_tile(html.Div('This is a test'), 'test container', 4),
    renders.render_tile(html.Div('This is a test'), 'test container', 4),
    renders.render_tile(html.Div('This is a test'), 'test container', 4)
]

layout = html.Div(
    className='main',
    children=[
        navbar.navbar,
        renders.render_container(tiles)
    ])