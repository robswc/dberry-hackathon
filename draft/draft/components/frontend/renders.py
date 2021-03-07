import dash_html_components as html
import time


def render_container(tiles):
    """
    Renders a container, that contains tiles.
    :return: html.Div
    """
    container = html.Div(
        className='container-fluid',
        style={'padding': '1em'},
        children=[
            html.Div(
                className='row',
                children=tiles,
            )
        ]
    )

    return container


def render_tile(obj, title, col):
    """
    Renders html, using bootstrap grids
    :return:
    """
    container = html.Div(
        style={'height': '90vh'},
        children=[
            html.Div(
                className='container-inner',
                children=[
                    html.H1(title),
                    html.Div(obj)
                ])

        ], className='container col-lg-{}'.format(col))

    return container
