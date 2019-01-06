#Read in data using the binance api
#Prints the data


from urllib.request import urlopen
import json
import pandas as pd

with urlopen('https://api.binance.com/api/v1/klines?symbol=LTCBTC&interval=1m') as resp:
    source = resp.read() # source is just a string




df = pd.read_json(source)
# data = json.loads(source) #parsed json, data is a python dic
#
# df = pd.DataFrame(data)
df.columns=[        'Open_time',
                    'Open',
                    'High',
                    'Low',
                    'Close',
                    'Volume',
                    'Close_time',
                    'Quote asset volume',
                    'Number_of_trades',
                    'Taker_buy_base_asset_volume',
                    'Taker_buy_quote_asset_volume',
                    'Ignore']
print(df)
