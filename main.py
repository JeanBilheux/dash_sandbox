import dash
from dash import html
import dash_bootstrap_components as dbc


external_stylesheets = [dbc.themes.CYBORG, "assets/style.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                meta_tags=[{'name': 'viewpoert',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=4, minimum-scale=0.5'}])

image_logo = 'team_logo.png'

app.layout = html.Div([
    dbc.Navbar([
            dbc.Row([
                dbc.Col([
                    html.A(
                    html.Img(src=app.get_asset_url(image_logo),
                             height="60px",
                             ),
                    href="/",
                    )],
                ),
                dbc.Col(html.Pre(" ")),
                dbc.Col(html.H1("NE"),
                        width="auto"),
                dbc.Col(html.H5("utron "),
                        width="auto"),
                dbc.Col(html.Pre("  ")),
                dbc.Col(html.H1("I")),
                dbc.Col(html.H5("maging ")),
                dbc.Col(html.Pre("  ")),
                dbc.Col(html.H1("T")),
                dbc.Col(html.H5("oolbox")),
                dbc.DropdownMenu(
                        label="Tools",
                        children=[
                            dbc.DropdownMenuItem("Neutron Transmission"),
                            dbc.DropdownMenuItem("Neutron Resonance"),
                            dbc.DropdownMenuItem("Composition Converter"),
                            dbc.DropdownMenuItem("Time of flight plotter"),
                            dbc.DropdownMenuItem("Bragg edge simulator"),
                            dbc.DropdownMenuItem("Golden angles"),
                        ],
                        color="primary",
                        size="lg",
                )
            ],
        align="center"),
    ],
    id="navbar",
    color="black",
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
