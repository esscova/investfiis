import pandas as pd

def cleanData(df):   

    df['DY'] = df['DY'].str.replace('-','0')
    df['DY'] = df['DY'].str.replace('.','')
    df['DY'] = df['DY'].str.replace(',','.')
    df['DY'] = df['DY'].astype(float)

    df['Nome'].fillna('-', inplace=True)

    categorias = {
    'Fiagro: ':'Fiagro',
    'Fiagro: Fiagro':'Fiagro',
    'Tijolo: Shoppings':'Tijolo',
    'Outros: Indefinido':'Outros',
    'Papel: Papéis':'Papel',
    'Tijolo: Lajes Corporativas':'Tijolo',
    'Sem categoria: ':'Outros',
    'Papel: Fundo de Fundos':'Papel',
    'Fundo Misto: Misto':'Fundo Misto',
    'Tijolo: Imóveis Residenciais':'Tijolo',
    'Fundos Imobiliários: ':'Outros',
    'Tijolo: Imóveis Industriais e Logísticos':'Tijolo',
    'Fundo Misto: Indefinido':'Fundo Misto',
    'Tijolo: Imóveis Comerciais - Outros':'Tijolo',
    'Tijolo: Agências de Bancos':'Tijolo',
    'Tijolo: Hotéis':'Tijolo',
    'Fundo Misto: Fundo de Desenvolvimento':'Fundo Misto',
    'Papel: ':'Papel',
    'Tijolo: Varejo':'Tijolo',
    'Tijolo: Fundo de Desenvolvimento':'Tijolo',
    'Tijolo: Educacional':'Tijolo',
    'Tijolo: Hospitalar':'Tijolo',
    'Fundo Misto: ':'Fundo Misto',
    'Tijolo: ':'Tijolo',
    'Outros: Fundo de Desenvolvimento':'Outros',
    'Fundos Imobiliários: Fundos Imobiliários':'Outros',
    'Fundo Misto: Papéis':'Fundo Misto'
    }
    df.Categoria = df.Categoria.map(categorias)
    return df

