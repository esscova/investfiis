from dash import Dash, html, dcc, Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd

# modulo que faz scraping retornando DataFrame Pandas
from services.getData import getData 

# modulo com layout a ser renderizado
from src.layouts import index

# dados
df = getData()

# app
app = Dash(__name__)
server = app.server
app.layout = index.layout

# callbacks
# graficos e card total
@app.callback(
    [
        Output('fundos-totais-selecionados','children'),
        Output('gr-fundos-selecionados','figure'),
        Output('gr-top-10','figure'),
        Output('gr-distribuicao','figure'),
        Output('gr-means','figure'),
    ],

    [
        Input('dy-range', 'value'),
        Input('dy-categorias','value')
    ]
)
def update(range,categorias):

    # selecionando dados conforme inputs
    df_filtered = df[df['Categoria'].isin(categorias)]
    df_final = df_filtered[(df_filtered['DY'] > range[0]) & (df_filtered['DY'] <= range[1])]

     
    # criando graficos conforme dados selecionados    
    # fundos selecionados
    fig = px.bar(df_final, y='DY', x='Ticker',color='DY',title='Fundos')
    fig.update_layout(xaxis={'tickangle':45})
    fig.update_layout(transition_duration=500)

    # top-10
    df_top = df_final.sort_values(by='DY',ascending=False).head(10)
    figTop = px.bar(df_top, x='DY',y='Ticker',title='Top-10')
    figTop.update_layout(transition_duration=500)

    # pizza 
    df_pie = df_final['Categoria'].value_counts()
    figPie = px.pie(names=df_pie.index, values=df_pie.values,title='Distribuição por Categoria')
    figPie.update_layout(transition_duration=500)

    # medias dy por categoria
    df_means = df_final.groupby('Categoria')['DY'].mean().reset_index()
    figMeans = px.line(df_means,y='DY',x='Categoria',markers='o',title='DY médio por categoria')
    figMeans.update_layout(transition_duration=500)
    
    return df_final.shape[0],fig,figTop,figPie,figMeans

# download CSV
@app.callback(
        Output("download", "data"), 
        Input("btn", "n_clicks")
        )

def download(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return dcc.send_data_frame(
            df.to_csv, "dataset.csv", index=False, encoding="utf-8-sig"
        )

if __name__ == "__main__":
    app.run(debug=True)
