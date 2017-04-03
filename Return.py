# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:41:11 2017

@author: Administrator
"""
period = range(0,756)
import r
import numpy as np

def lmReturn(alpha,beta): 
    R = []
    for i in period:
        R.append(r.r(alpha,beta,i))
    return np.mean(R)
   
def func(x):
    return lmReturn(x[0], x[1])