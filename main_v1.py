import dash
from dash import html
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.CYBORG, "assets/style.css"]
#external_stylesheets = [dbc.themes.CYBORG]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=10, minimum-scale=0.5'}])

image_logo = 'team_logo.png'

app.layout = html.Div([
                dbc.Row([
                    html.A(
                        html.Img(src=app.get_asset_url(image_logo),
                                 height="60px"),
                        href="/",
                    ),
                    dbc.Col([html.Pre(" ")]),
                    dbc.Col(html.H1("NE")),
                    dbc.Col(html.H5("utron ")),
                    dbc.Col(html.Pre("  ")),
                    dbc.Col(html.H1("I")),
                    dbc.Col(html.H5("maging ")),
                    dbc.Col(html.Pre("  ")),
                    dbc.Col(html.H1("T")),
                    dbc.Col(html.H5("oolbox")),
                    
                ],
                ),
            ])

if __name__ == '__main__':
    app.run_server(debug=True)
