import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc


df = pd.read_csv('INTC2018.csv')

df['Date'] = df['Date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

df['Date'] = df['Date'].map(mdates.date2num)
ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']]

ma_day = [5, 10, 20, 50]

for ma in ma_day:
    col_name = "SMA%s" % (str(ma))
    df[col_name] = df['Adj Close'].rolling(window=ma, center=False).mean()


plt.figure(figsize=(10, 5))
top = plt.subplot2grid((4,4), (0, 0), rowspan=3, colspan=4)


candlestick_ohlc(top, ohlc.values, width=0.6, colorup='green', colordown='red')

top.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))


top.plot(df['Date'], df['SMA5'], color='yellow', label='SMA5')
top.plot(df['Date'], df['SMA10'], color='blue', label='SMA10')
top.plot(df['Date'], df['SMA20'], color='pink', label='SMA20')
top.plot(df['Date'], df['SMA50'], color='brown', label='SMA50')

top.legend(loc='best')
top.set_title('INTC chart with volume')
#top.axes.get_xaxis().set_visible(False)


bottom = plt.subplot2grid((4,4), (3,0), colspan=4, rowspan=1)
bottom.bar(df.index, df['Volume'])
bottom.set_ylabel('Volume')


plt.tight_layout()
plt.show()





