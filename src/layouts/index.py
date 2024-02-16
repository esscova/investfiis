from dash import html, dcc

from services.getData import getData

from src.components import (
    AsideLogo,
    RangeSlider,
    Dropdown,
    DownloadBtn,
    Nav,
    Card,
)
df = getData()
layout = html.Div(
    [
        html.Aside(
            [
                AsideLogo.layout,
                DownloadBtn.layout,
                Nav.layout,
            ]
        ),
        html.Main(
            [
                # linha 1
                Dropdown.layout,
                RangeSlider.layout,
                # linha 2
                Card.layout('Fundos selecionados',html.Span(id='fundos-totais-selecionados')),
                Card.layout('Não pagantes',df[df['DY']==0].shape[0]),
                Card.layout('Descartados',df[df['DY']>37].shape[0]),
                #linha 3
                dcc.Graph(id="gr-fundos-selecionados"),
                dcc.Graph(id="gr-top-10"),
                dcc.Graph(id="gr-distribuicao"),
                dcc.Graph(id="gr-means"),
            ]
        ),
    ],
    className="render",
)
