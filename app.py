import dash
import dash_bootstrap_components as dbc


external_stylesheets = [dbc.themes.COSMO, "assets/style.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, '
                                       'initial-scale=1.0, '
                                       'maximum-scale=4, '
                                       'minimum-scale=0.5'}])
app.config.suppress_callback_exceptions = True
