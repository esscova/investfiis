from dash import Dash, html, dash_table, dcc, Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd
import urllib.parse
from services.getData import getData

# load
df = getData()

# initialize
app = Dash(__name__)

app.layout = html.Div(id='main',children=[

    html.Div(className='slider',children=[
         html.H2('DY'),
         dcc.RangeSlider(
              id='dy-range-slider',
              min=0,
              max=30,
              value=[0,35],
              step=1,
              marks={0:'0',5:'5',10:'10', 15:'15', 20:'20', 25:'25',30:'30',35:'35'}
         ),
         html.Button("Download Dataset",id='btn'),
         dcc.Download(id='download')
    ]),
    html.Div(className='graphs',children=[
         dcc.Graph(id='top'),
         dcc.Graph(id='top-categ'),
         dcc.Graph(id='dist'),
         dash_table.DataTable(id='table',data=df.to_dict('records'),page_size=10)
    ]),
])

# callbacks ===========


@app.callback(

     Output('download','data'),
     Input('btn','n_clicks')
)
def download(n_clicks):
     if n_clicks is None:
          raise PreventUpdate
     else:
          return dcc.send_data_frame(df.to_csv, "dataset.csv", index=False, encoding='utf-8-sig')


@app.callback(

     [Output('top','figure'),
      Output('top-categ','figure'),
      Output('dist','figure')],
     
     Input('dy-range-slider','value')
)

def update_figure(selected_dy):
     filtered_df = df[(df.DY > selected_dy[0]) & (df.DY <= selected_dy[1])]
     
     fig1 = px.bar(filtered_df.nlargest(15, 'DY'), x='DY',y='Ticker', title='TOP 15 Dividend Yield')
     fig1.update_layout(transition_duration=500)
     
     fig2 = px.bar(filtered_df.groupby('Categoria').size().reset_index(name='Count'), x='Categoria', y='Count', title='Fundos por categoria')
     fig2.update_layout(transition_duration=500)  

     category_counts = filtered_df['Categoria'].value_counts()
     fig3 = px.pie(names=category_counts.index, values=category_counts.values, title='Fundos por categoria')
     fig3.update_layout(transition_duration=500)

     
     return fig1, fig2, fig3

# run ==========
if __name__ == '__main__':
     app.run(debug=True)
