import dash_html_components as html

# Navbar
from components.navbar import navbar

# Components
from components.frontend import renders

# Interfaces
from components.frontend import image_upload_interface
from components.frontend import input_interface

img_upload = image_upload_interface.render()
input_module = input_interface.render()

tiles = [
    renders.render_tile(img_upload, 'Image', 4),
    renders.render_tile(input_module, 'Input', 4),
    renders.render_tile(html.Div('Library'), 'Library', 4)
]

layout = html.Div(
    className='main',
    children=[
        navbar.navbar,
        renders.render_container(tiles)
    ])