from dash import html


def layout(texto,dados):
    return html.Div([html.P(texto), html.Span(dados)],className='card')
