import requests
import json
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

nasdaqLs = []
companies=requests.get('https://pkgstore.datahub.io/core/s-and-p-500-companies/constituents_json/data/64dd3e9582b936b0352fdd826ecd3c95/constituents_json.json')
companies=json.loads(companies.text)
for i in companies:
    nasdaqLs.append(i['Symbol'])
print(nasdaqLs)

for i in nasdaqLs:
    api_key='T7DNCV4J6KQJUPS8'
    try:
        data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + i + '&interval=60min&apikey=' + api_key)
        data=data.json()
        data=data['Time Series (60min)']
        print('\n\n' + i + '\n\n')
        print(data)
    except:
        try:
            data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + i + '&interval=30min&apikey=' + api_key)
            data=data.json()
            data=data['Time Series (30min)']
            print('\n\n' + i + '\n\n')
            print(data)
        except:
            try:
                data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + i + '&interval=15min&apikey=' + api_key)
                data=data.json()
                data=data['Time Series (15min)']
                print('\n\n' + i + '\n\n')
                print(data)
            except:
                try:
                    data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + i + '&interval=5min&apikey=' + api_key)
                    data=data.json()
                    data=data['Time Series (5min)']
                    print('\n\n' + i + '\n\n')
                    print(data)
                except:
                    try:
                        data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + i + '&interval=1min&apikey=' + api_key)
                        data=data.json()
                        data=data['Time Series (1min)']
                        print('\n\n' + i + '\n\n')
                        print(data)
                    except:
                        print('\n\n\n\nerror\n\n\n\n')