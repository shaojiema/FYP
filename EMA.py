import pandas as pd

df0 = pd.read_csv('pricedata.csv')
df0 = df0.set_index(df0['stocks'])
df0 = df0.iloc[:, 1:-1]
df1 = df0.loc['AAPL']       
#print len(df1['2013/3/1':'2016/3/1'])
print df1
def ema(alpha,beta,i): #input price matrics
    pricematrix = df1[i:i+20]

    global s_alpha
    s_alpha = []
    s_alpha.append(pricematrix[0])
    for j in range(1, len(pricematrix)):
        s_alpha.append(pricematrix[j]*alpha + s_alpha[j - 1]*(1 - alpha))


    global s_beta
    s_beta = []
    s_beta.append(pricematrix[0])
    for j in range(1, len(pricematrix)):
        s_beta.append(pricematrix[j] * beta + s_beta[j - 1] * (1 - beta))

    d = s_alpha[-1] - s_beta[-1]

    return d
    #return \d,s_alpha,s_beta
















