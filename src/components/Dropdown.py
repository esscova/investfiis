from dash import html,dcc
import pandas

from services.getData import getData

df = getData()

categorias = list(df["Categoria"].unique())
layout = html.Div(
    [
        html.Label("Categorias"),
        dcc.Dropdown(categorias, categorias, multi=True, id="dy-categorias"),
    ],
    className='drop'
)
