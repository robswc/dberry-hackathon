import dash_html_components as html

# Navbar
from components.navbar import navbar

# Components
from components.frontend import renders

# Interfaces
from components.frontend import image_upload_interface
from components.frontend import input_interface
from components.frontend.library_interface import li

# Book
from components.backend.book import Book

img_upload = image_upload_interface.render()
input_module = input_interface.render()

# Make library
li.create_library('default')
# li.get_library('default').add_book(Book(title='Harry Potter', authors=['JK Rowling'], isbn='111'))
li.get_library('default').load_library()

tiles = [
    renders.render_tile(img_upload, 'Image', 4),
    renders.render_tile(input_module, 'Input', 4),
    renders.render_tile(li.render(li.get_library('default')), 'Library', 4)
]

layout = html.Div(
    className='main',
    children=[
        navbar.navbar,
        renders.render_container(tiles)
    ])