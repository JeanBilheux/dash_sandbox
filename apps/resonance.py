from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

from main_app import app

layout = html.Div([
    html.H3("this is the resonance page"),
    dbc.Button("Submit", id='clustering_submit_button'),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'),
              Input('clustering_submit_button', 'n_clicks'))
def clustered_map(n_clicks):
    return f"button has been clicked {n_clicks}"

