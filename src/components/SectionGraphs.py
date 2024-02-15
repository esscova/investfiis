from dash import html, dcc

layout = html.Section(
    [
        dcc.Graph(id='gr-hist'),
        dcc.Graph(id='gr-pie'),
        dcc.Graph(id='gr-bar')

    ],className='graphs')