#!/usr/bin/env python3
# built on 09/08/2018
# pip install mpl_finance


import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc


df = pd.read_csv('AMD.csv')
print(df.info())
print(df.head())

###df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

df['Date'] = df['Date'].map(mdates.date2num)
ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']]

df['ema5'] = df['Close'].ewm(span=5, adjust=False).mean()
df['ema10'] = df['Close'].ewm(span=10, adjust=False).mean()
df['ema20'] = df['Close'].ewm(span=20, adjust=False).mean()
df['ema50'] = df['Close'].ewm(span=50, adjust=False).mean()

fig, ax = plt.subplots(figsize=(12, 5))

candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

ax.plot(df['Date'], df['ema5'], color='yellow', label='EMA5')
ax.plot(df['Date'], df['ema10'], color='blue', label='EMA10')
ax.plot(df['Date'], df['ema20'], color='pink', label='EMA20')
ax.plot(df['Date'], df['ema50'], color='brown', label='EMA50')

ax.legend(loc='best')



plt.savefig('AMD chart with EMA')
plt.show()

##SMA using rolling

#ma_day = [5, 10, 20, 50]
#for ma in ma_day:
#    col_name = "SMA%s" % (str(ma))
#    df[col_name] = AMD['Adj Close'].rolling(window=ma, center=False).mean()


###Monte Carlo simulation

# days = 100
# dt = 1/100
# mu = AMD.mean()['Adj Close']
# sigma = AMD['Adj Close'].std()
#
#
# def stock_monte_carlo(start_price, days, mu, sigma):
#     price = np.zeros(days)
#     price[0] = start_price
#
#     shock = np.zeros(days)
#     drift = np.zeros(days)
#
#     for x in range(1, days):
#         shock[x] = np.random.normal(loc=mu*dt, scale=sigma*np.sqrt(dt))
#
#         drift[x] = mu * dt
#
#         price[x] = price[x-1] + (price[x-1] * (drift[x] + shock[x]))
#
#     return price
#
# start_price = 11.49
#
# for run in range(100):
#     plt.plot(stock_monte_carlo(start_price, days, mu, sigma))
#
#
# runs = 1000
#
# simulations = np.zeros(runs)
#
#for run in range(runs):
#    simulations[run] = stock_monte_carlo(start_price,days,mu,sigma)[days-1]
#
# q = np.percentile(simulations,1)
# plt.hist(simulations,bins=200)
# plt.figtext(0.6,0.8,s="Start price: $%.2f" %start_price)
# plt.figtext(0.6,0.7,"Mean final price: $%.2f" % simulations.mean())
# plt.figtext(0.6,0.6,"VaR(0.99): $%.2f" % (start_price -q,))
# plt.figtext(0.15,0.6, "q(0.99): $%.2f" % q)
# plt.axvline(x=q, linewidth=4, color='r')
# plt.title(u"Final price distribution for Google Stock after %s days" %days, weight='bold')
# plt.show()

