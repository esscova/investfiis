from dash import html, dcc

layout = html.Div(
    [
        html.Label("Dividend Yield"),
        dcc.RangeSlider(
            id="dy-range",
            min=0.1,
            max=36,
            value=[10, 25],
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
    ],className='range'
)
