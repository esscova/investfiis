from dash import html, dcc

from services.getData import getData

from src.components import (
    RangeSlider,
    Dropdown,
    DownloadBtn,
    Nav,
    Card,
)

df = getData()
layout = html.Div(
    [   
        html.Img(src="../../assets/img/logo.png",
            className='logo'),
        
        html.Div(
            [
                html.H1('DASHBOARD'),
                DownloadBtn.layout,
            ],
            className='title'
        ),

        Dropdown.layout,
        RangeSlider.layout,

        html.Div(
            [
                Card.layout(
                    "Fundos selecionados",
                    html.Span(id="fundos-totais-selecionados"),
                ),
                Card.layout("Não pagantes", df[df["DY"] == 0].shape[0]),
                Card.layout("Descartados", df[df["DY"] > 37].shape[0]),
            ],
            className="cards",
        ),

        dcc.Graph(id="gr-top-10"),
        dcc.Graph(id="gr-distribuicao"),
        dcc.Graph(id="gr-fundos-selecionados"),
        dcc.Graph(id="gr-means"),
        Nav.layout,
    ],
    className="root",     
)
