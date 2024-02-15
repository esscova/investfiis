from dash import html, dcc

layout = html.Section(
    [
        dcc.Graph(id='gr-fundos-selecionados'),
        dcc.Graph(id='gr-top-10'),
        dcc.Graph(id='gr-distribuicao'),
        dcc.Graph(id='gr-means')

    ],className='graphs')