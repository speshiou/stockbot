import os, sys, datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(ROOT_DIR, "pylib"))

from pandas_datareader import data as pdr
import yfinance as yf

targets = [ "1101.TW", "1102.TW", "1103.TW", "1104.TW", "1108.TW", "1109.TW" ]

today = datetime.date.today()
start = datetime.datetime.now() - datetime.timedelta(days=1095)
end = datetime.date.today()

yf.pdr_override()

data = pdr.get_data_yahoo(targets, start, end)
buy = []
for i in data['Close'].columns:
    print(i)
    deviation_level = data['Close'][i].mean() - data['Close'][i].std() * 2
    print(deviation_level)
    if deviation_level > data['Close'][i].iloc[len(data['Close'][i]) - 1]:
        buy.append(i)
print(buy)

