import pandas as pd
import numpy as np
df1=pd.read_csv('pricedata.csv')
#print df1[4:5]
#print '-------index:-------------'
#print df1.index
#print '-------columns:-------------'
#print df1.columns
df1 = df1.set_index(df1['stocks'])
df1 = df1.iloc[:, 1:-1]
print df1.shape
#print df1.index
#print df1.columns