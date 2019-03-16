import requests
import json
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

# allStocks = []

# nasdaq = []
# companies=requests.get('https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_json/data/a5bc7580d6176d60ac0b2142ca8d7df6/nasdaq-listed_json.json')
# companies=json.loads(companies.text)
# for i in companies:
#     nasdaq.append(i['Symbol'])
#     allStocks.append(i['Symbol'])
# print(nasdaq)

# sp500 = []
# companies=requests.get('https://pkgstore.datahub.io/core/s-and-p-500-companies/constituents_json/data/64dd3e9582b936b0352fdd826ecd3c95/constituents_json.json')
# companies=json.loads(companies.text)
# for i in companies:
#     sp500.append(i['Symbol']) 
#     if i['Symbol'] not in allStocks:
#         allStocks.append(i['Symbol'])
# print(sp500)


allStocks = []
companiesFile = open('companies.txt', 'r') 
for i in companiesFile.readlines():
    # print('-'+i.strip()+'-')
    allStocks.append(i.strip())
companiesFile.close()

stockSave = open('StockSaveFile.txt', 'w')
# for sym in allStocks:
#     stockSave.write(sym + ': \n')

for sym in allStocks:
    try:
        data = requests.get('https://cloud.iexapis.com/beta/stock/' + sym + '/price/tops?token=pk_e265e327db174888b061f8744778a738')
        data = json.loads(data.text)
        print(sym + ':', data)
    except:
        print('error:', sym)

stockSave.close()




# companiesFile = open('companies.txt', 'r') 
# for i in companiesFile.readlines():
#     symbolEnd = i.find(':')
#     symbol = i[0:symbolEnd]


# companiesFile.close()




# df_close = pd.DataFrame()
# df_temp = pd.read_json('https://cloud.iexapis.com/beta/stock/' + 'aapl' + '/price/tops?token=pk_e265e327db174888b061f8744778a738')
# print(df_temp.head(4))



# while (0):

    # for sym in sp500:
    #     df_close = pd.DataFrame()
    #     df_temp = pd.read_json('https://cloud.iexapis.com/beta/tops?token=pk_e265e327db174888b061f8744778a738&symbols=' + sym)
    #     print(df_temp.head(4))