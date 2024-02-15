from dash import Dash, html, dcc, Input, Output
from dash.exceptions import PreventUpdate
import pandas as pd

#from app import *
from services.getData import getData

df = getData()
categorias = list(df["Categoria"].unique())

layout = html.Aside(
    [
        html.Img(src="../../assets/img/logo.png"),
        html.H2("Fundos Imobiliários"),
        html.Label("Escolha as margens de DY"),
        dcc.RangeSlider(
            id="dy-range",
            min=0.1,
            max=36,
            value=[5, 25],
            step=5,
            marks={
                0.1: "Min",
                5: "5",
                10: "10",
                15: "15",
                20: "20",
                25: "25",
                30: "30",
                36: "Max",
            },
        ),
        html.Label("Escolha fundos por categoria"),
        dcc.Dropdown(categorias, categorias, multi=True, id="dy-categorias"),
        html.Button("Download CSV", id="btn"),
        dcc.Download(id="download"),
    ]
)
