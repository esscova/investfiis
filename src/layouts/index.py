from dash import Dash, html, dcc

from src.components import Aside, Main

layout = html.Div([
    Aside.layout,
    Main.layout,

],className='render')