# tested DataReader on 09/08/2018
# Yahoo works again
# Google is not working

import pandas_datareader.data as web
import pandas as pd
import datetime


start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2018, 8, 31)

data = web.DataReader('AMD', 'yahoo', start, end)
df = pd.DataFrame(data)
df.to_csv('AMD.csv')
