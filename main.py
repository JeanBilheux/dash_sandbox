import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


external_stylesheets = [dbc.themes.CYBORG, "assets/style.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                meta_tags=[{'name': 'viewpoert',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=4, minimum-scale=0.5'}])

app.layout = html.Div([
    dbc.Row([
        html.H1("NE"),
        html.H5("utron "),
        html.H1("I"),
        html.H5("maging "),
        html.H1("T"),
        html.H5("oolbox"),
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
