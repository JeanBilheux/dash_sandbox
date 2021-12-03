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
                html.A(
                    html.Img(src=app.get_asset_url(image_logo),
                             height="60px"),
                    href="/",
                ),
                html.Pre(" "),
                html.H1("NE"),
                html.H5("utron "),
                html.Pre("  "),
                html.H1("I"),
                html.H5("maging "),
                html.Pre("  "),
                html.H1("T"),
                html.H5("oolbox"),
                ],
            align="center",
            class_name="row_nav_bar",
            ),
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
    id="navbar",
    color="black",
    expand="lg",
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
