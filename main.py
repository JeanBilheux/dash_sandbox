import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Output, Input, State

from apps import resonance, transmission, converter, tof_plotter, bragg, golden_angles
from config import app_dict


external_stylesheets = [dbc.themes.COSMO, "assets/style.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                meta_tags=[{'name': 'viewpoert',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=4, minimum-scale=0.5'}])

image_logo = 'team_logo.png'


home_page = html.Div([
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
                    dbc.Col(html.Pre(""),
                            class_name="header_pre_padding"),
                    dbc.Col(html.H1("NEU"),
                            width="auto",
                            class_name="header_col_right_padding"),
                    dbc.Col(html.H5("tron"),
                            width="auto"),
                    dbc.Col(html.Pre(""),
                            class_name="header_pre_padding"),
                    dbc.Col(html.H1("I"),
                            class_name="header_col_right_padding"),
                    dbc.Col(html.H5("maging"),
                            class_name="header_col_left_padding_special_case_for_i"),
                    dbc.Col(html.Pre(""),
                            class_name="header_pre_padding"),
                    dbc.Col(html.H1("T"),
                            class_name="header_col_right_padding"),
                    dbc.Col(html.H5("oolbox"),
                            class_name="header_col_left_padding"),
                    dbc.Col(html.Pre(""),
                            class_name="header_dropdown_separator"),
                    ],
                    align="center"),
                dbc.DropdownMenu(
                        label="Select a Tool",
                        id="list_of_tools_dropdown",
                        children=[
                            dbc.DropdownMenuItem("Neutron Transmission", href="/transmission"),
                            dbc.DropdownMenuItem("Neutron Resonance", href="/resonance"),
                            dbc.DropdownMenuItem("Composition Converter", href="/converter"),
                            dbc.DropdownMenuItem("Time of flight plotter", href='/tof_plotter'),
                            dbc.DropdownMenuItem("Bragg edge simulator", href='/bragg'),
                            dbc.DropdownMenuItem("Golden angles", href='/golden_angles'),
                        ],
                        color="primary",
                        size="lg",
                ),
            ],
            class_name="header_format",
            color="white",
        ),
    dcc.Location(id='location'),
    html.Hr(style={'borderTop': '3px solid blue'}),
    html.Div(id='tool_selected_page'),
    html.Div(id='main_content')
])
app.layout = home_page


# @app.callback(
#     Output('app1_iso_check', 'style'),
#     [
#         Input('app1_iso_check', 'value'),
#     ],
#     [
#         State('app1_iso_input', 'style'),
#     ])
# def show_hide_iso_table(iso_changed, style):
#     if len(iso_changed) == 1:
#         style['display'] = 'block'
#     else:
#         style['display'] = 'none'
#
#     print("in show_hide_iso_table")
#     return style


@app.callback(Output('main_content', 'children'),
              Input('location', 'pathname'))
def fill_main_content(pathname):
    if pathname is None:
        return "Loading ..."

    for _key in app_dict.keys():
        if app_dict[_key]['url'] == pathname:
            return eval(f"{_key}.layout")
    if pathname == '/':
        ""
    else:
        return '404: URL not founds!'


if __name__ == '__main__':
    app.run_server(debug=True)
