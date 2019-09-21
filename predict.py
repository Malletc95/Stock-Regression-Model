import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta

stock = pd.read_csv('sphist.csv')
stock['Date'] = pd.to_datetime(stock['Date'])
stock = stock.sort_values(by = 'Date')

short_stock = stock.head()

#for index, row in short_stock.iterrows():
date = stock.iloc[10,:]


# print(date)
# print('\n')
#print((stock['Date'] > date['Date'] + timedelta(days  = -5)) & (stock['Date'] < date['Date']))
print(stock['Date'].head(20))    



