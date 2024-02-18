from dash import html,dcc

layout = html.Div(
    [
        html.Button("Download CSV", id="btn"),
        dcc.Download(id="download")
    ],
    className='btn-download'
)