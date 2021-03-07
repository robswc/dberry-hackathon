import dash_html_components as html
import dash_core_components as dcc

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
# li.get_library('default').load_library()

md = dcc.Markdown(
    '''
    # d.berry - an online library asset manager 

    #### This application concept was concieved, developed, and presented in < 24 hours by Robert Carroll and Brandon Frulla for the Spring 2021 UMW ACM Hackathon

    This application leverages Dash with the Google Books API, as well as google OCR to parse books titles from a photograph and add them to the user's library.

    [Contributions to the code base can be made here.](http://https://github.com/robswc/dberry-hackathon/tree/master/draft "Contributions to the code base can be made here.")
    
    '''
)

layout = html.Div(
    className='main',
    children=[
        navbar.navbar,
        renders.render_container(md)
    ])