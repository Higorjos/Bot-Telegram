import requests
from bs4 import BeautifulSoup
import pandas as pd
import re 
import json

response = requests.get('https://www.moneytimes.com.br/cotacoes/moedas/')
content = response.content
site = BeautifulSoup(content, "html.parser")

class scrap_cotacoes:
    
    def __init__(self):

table = site.findAll('div', attrs= {'class': 'cross-table__table-row'})

df = []
for moeda in table:
    titulo = moeda.find('div', attrs= {'class': 'cell large-24 medium-12 small-12 data-cotacao__ticker_name'})

    cotacao = moeda.find('div', attrs= {'class': 'cell auto data-cotacao__ticker_quote'})
    
    if (titulo):
     df.append([titulo.text, cotacao.text])

cotacoes = pd.DataFrame(df, columns=['Moeda', 'Cotação'])
print(cotacoes)





