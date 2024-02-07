from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd
from services.getData import getData

# load
df = getData()


# initialize
app = Dash(__name__)

app.layout = html.Div(id='root',children=[
     
    html.Header([
        html.Div(className='left', children=[
            html.H2('Dashboard financeiro'),     
            html.H1('Fundos imobiliários'), 
        ]),
         html.Div(className='right', children=[
            html.H3('Bem vindo à minha dashboard'),     
            html.P('Confira meus contatos'),
            html.A('Linkedin',href='https://www.linkedin.com/in/wellington-moreira-santos', target='_blank'),
            html.A('GitHub',href='https://github.com/wellington-moreira-santos',target='_blank') 
        ])  
        
    ]),

    html.Div([
         html.H2('DY'),
         dcc.RangeSlider(
              id='dy-range-slider',
              min=0,
              max=30,
              value=[6,12],
              step=None,
              marks={0:'0',5:'5',10:'10', 15:'15', 20:'20', 30:'20+'}
         )
    ]),

      
    html.Section(className='S-cards',children=[
         
        html.Div(className='flex-card',children=[
                html.Div(className='card',children=['Fundos',
                    html.Span(className='valor',children=[f'{ df.shape[0] }'])   
                    ]),
                html.Div(className='card',children=['Título',
                    html.Span([f'{round(df.DY.mean())}'])   
                    ]),
                html.Div(className='card',children=['Título',
                    html.Span([f'{round(df.DY.mean())}'])   
                    ]),
                html.Div(className='card',children=['Título',
                    html.Span([f'{round(df.DY.mean())}'])   
                    ])
        ]), 
    ]),

    html.Div(className='flex',children=[  
                               
        html.Div(className='tabela',
            children=[          
                dcc.Graph(figure=px.bar(
                    df.query('DY <= 36 & DY != 0').nlargest(10,'DY'),
                    x='DY',
                    y='Ticker'
                ))        
        ]),
                
        html.Div(className='histograma',
            children=[
                dcc.Graph(figure=px.histogram(
                                df.query('DY <= 36 & DY != 0 '),
                                x='Categoria',
                                y='DY',
                                histfunc='count'))
        ])
    ]),
    html.Div(className='tabela',
            children=[          
                dash_table.DataTable(data=df.to_dict('records'),page_size=10)])
])

# run
if __name__ == '__main__':
     app.run(debug=True)
