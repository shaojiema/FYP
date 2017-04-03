# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:31:02 2017

@author: Administrator
"""

import piecewise as p
from sympy import *
import pandas as pd

df0 = pd.read_csv('pricedata.csv')
df0 = df0.set_index(df0['stocks'])
df0 = df0.iloc[:, 1:-1]
df1 = df0.loc['AAPL']       #data indexing, choosing 'AAPL'

w0 = 0.01

def r(alpha,beta,i):
    P1 = df1[i+20]
    P0 = df1[i+19]
    piecewise = p.piecewise(alpha,beta,i)
    r =w0 / (piecewise+w0) + piecewise / (w0 + piecewise) *P1 / P0
    return r-1
