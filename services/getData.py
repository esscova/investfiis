import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from services.cleanData import cleanData

def getData ():
    URL = 'https://fiis.com.br/lista-de-fundos-imobiliarios/'

    HEADER = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        page = requests.get(URL, headers=HEADER)
        page.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
        return
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        return
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        return
    except requests.exceptions.RequestException as err:
        print ("Something went wrong with the request:",err)
        return

    site = bs(page.content,'html.parser')
    divs = site.find_all('div',{"class":"tickerBox"})
    dados = [
      {
          "Ticker": div.find('div', {"class": "tickerBox__title"}).text,
          "DY": div.find_all('div', {"class": "tickerBox__info__box"})[0].text,
          "Nome":div.find('div',{"class":"tickerBox__desc"}).text,
          "Categoria":div.find('span',{"class":"tickerBox__type"}).text
      }
      for div in divs
    ]
    df = pd.DataFrame(dados)
    
    return cleanData(df)
