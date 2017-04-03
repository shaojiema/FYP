import pandas_datareader.data as web
import datetime as dt
import pandas as pd
df1=pd.read_csv('S&P500index.csv')
stock=df1['Code']
start=dt.datetime(2014,11,30)
end= dt.datetime(2015,11,30)
df1=web.DataReader(stock,'yahoo',start,end)
df1['Volume'].T
df1['Volume'].T.sum(axis=1)
df2=df1['Volume'].T.sum(axis=1)
df3=df2.sort_values(ascending=False)
df3.to_csv('volume.csv')


