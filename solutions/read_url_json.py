import pandas as pd

url = ('https://data.cityofchicago.org/'
              'resource/cwig-ma7x.json?$limit=5')
pd.read_json(url, orient='records')
