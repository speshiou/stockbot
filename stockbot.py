import os, sys, datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(ROOT_DIR, "pylib"))

import pandas as pd
from pandas_datareader import data
import yfinance as yf

targets = [ "1101.TW", "1102.TW", "1103.TW", "1104.TW", "1108.TW", "1109.TW" ]

today = datetime.date.today()
start = datetime.datetime.now() - datetime.timedelta(days=1095)
end = datetime.date.today()

pd.core.common.is_list_like = pd.api.types.is_list_like
yf.pdr_override()

stock = data.get_data_yahoo(targets, start, end)
buy = []
for i in stock['Close'].columns:
    print(i)
    deviation_level = stock['Close'][i].mean() - stock['Close'][i].std() * 2
    print(deviation_level)
    if deviation_level > stock['Close'][i].iloc[len(stock['Close'][i]) - 1]:
        buy.append(i)
print(buy)

