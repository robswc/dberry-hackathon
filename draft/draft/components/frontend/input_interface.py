import dash_html_components as html
import dash_core_components as dcc


def render():
    img_upload = html.Div([
        dcc.Input()
    ])

    return img_upload
