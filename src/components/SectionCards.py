from dash import html
import pandas 
from services.getData import getData

df = getData()


layout = html.Section(
    [
        html.Div([html.P("Fundos selecionados"), html.P(id='total-fiis')], className="card-info"),
        html.Div([html.P("Fundos sem DY"), html.P(f'{df[df["DY"]==0].shape[0]}')], className="card-info"),
        html.Div([html.P("Fundos DY discrepantes"), html.P(f'{df[df["DY"]>=36].shape[0]}')], className="card-info"),
    ],className='cards'
)
