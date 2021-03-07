import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from PIL import Image, ImageFilter
from dash.exceptions import PreventUpdate
import dash
from dash.dependencies import Input, Output, State, MATCH, ALL
import cv2
import time
import uuid

# import app
from app import app


filelist = [
    "assets/img/test/example_image.jpg",
]


im = Image.open(filelist[0])

print('image size')
print(im.size)

fig = go.Figure()
fig.add_layout_image(
        x=0,
        sizex=int(im.size[0]),
        y=0,
        sizey=int(im.size[1]),
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        source=filelist[0]
)

fig.update_xaxes(showgrid=False, range=(0, im.size[0]))
fig.update_yaxes(showgrid=False, scaleanchor='x', range=(im.size[1], 0))
fig.update_layout(margin=dict(l=5, r=5, t=5, b=5))
fig.update_yaxes(visible=False, showticklabels=False)
fig.update_xaxes(visible=False, showticklabels=False)


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        return text.description

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

def render():
    img_upload = html.Div([
        dbc.Card(
            id="imagebox",
            children=[
                dbc.CardHeader(html.H5('Select Books')),
                dbc.CardBody(
                    [
                        dcc.Graph(
                            id="graph",
                            figure=fig,
                            config={"modeBarButtonsToAdd": ["drawrect", "eraseshape"]},
                        )
                    ]
                ),
            ],
        ),

        # Data section
        dbc.Card(
            [
                dbc.CardHeader(html.H6('Books')),
                dbc.CardBody(
                    [
                        dbc.Row(
                            dbc.Col([html.Div(id='annotations-table')

                                     ]),
                        ),
                        dbc.Row(dbc.Col([], align="center")
                                ),
                    ]
                ),
                dbc.CardFooter(
                    [
                        html.Div(
                            [
                                # We use this pattern because we want to be able to download the
                                # annotations by clicking on a button
                                html.A(
                                    id="download",
                                    download="annotations.json",
                                    # make invisble, we just want it to click on it
                                    style={"display": "none"},
                                ),
                                dbc.Button(
                                    "OCR Annotations", id="ocr-button", outline=True,
                                ),
                                html.Div(id="dummy", style={"display": "none"}),
                                # dbc.Tooltip(
                                #     "You can download the annotated data in a .json format by clicking this button",
                                #     target="download-button",
                                # ),
                            ],
                        )
                    ]
                ),
            ],
        )

    ])

    return img_upload

annotation_uids = []

def crop_image(img, coord):
    uid = str(uuid.uuid4()).split('-')[0]
    crop_area = (coord.get('x0'), coord.get('y0'), coord.get('x1'), coord.get('y1'))
    im1 = im.crop(crop_area)
    im1.save('assets/img/test/{}.jpg'.format(uid))
    return uid

@app.callback(
    [Output("annotations-table", "children")],
    [
        Input('ocr-button', 'n_clicks'),
        Input("graph", "relayoutData"),
    ],
)
def modify_table_entries(n_clicks, graph_relayoutData):
    cbcontext = [p["prop_id"] for p in dash.callback_context.triggered][0]
    print(cbcontext)
    if graph_relayoutData is None:
        print('PREVENTING UPDATE')
        raise PreventUpdate
    if cbcontext == "graph.relayoutData" and graph_relayoutData.get('shapes') is not None:

        x0 = round(graph_relayoutData.get('shapes')[-1].get('x0'), 2)
        x1 = round(graph_relayoutData.get('shapes')[-1].get('x1'), 2)
        y0 = round(graph_relayoutData.get('shapes')[-1].get('y0'), 2)
        y1 = round(graph_relayoutData.get('shapes')[-1].get('y1'), 2)

        print(x0, x1, y0, y1)
        annotation_uid = crop_image(im, {'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1})
        annotation_uids.append(annotation_uid)

    table_rows = []
    table_rows.append(html.Tr([html.Th('ID'), html.Th('PREVIEW'), html.Th('RESULT'), html.Th('ADD')]))
    if cbcontext == 'ocr-button.n_clicks':
        for a in annotation_uids:
            dt = detect_text('assets/img/test/{}.jpg'.format(a))
            table_rows.append(html.Tr([html.Td(a), html.Td(
                html.Img(src='assets/img/test/{}.jpg'.format(a), className='book-spine-thumbnail')),
                                       html.Td(dt),
                                       html.Td(html.Button('▸', id={'ocr-add': dt}))]))
    else:
        for a in annotation_uids:
            table_rows.append(html.Tr([html.Td(a), html.Td(
                html.Img(src='assets/img/test/{}.jpg'.format(a), className='book-spine-thumbnail')),
                                       html.Td('N/A'),
                                       html.Td()]))



    table = html.Div(
        children=[
            html.Table(table_rows, className='annotation-table')

    ])

    return [table]

