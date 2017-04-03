# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:11:33 2017

@author: Administrator
"""

import Return2 as R
import numpy as np

def derivative(vector,dx): 
    alpha =  vector[0]
    beta = vector[1]    
    global partial_alpha
    global partial_beta    
    partial_alpha = (R.lmReturn(alpha + dx,beta) - R.lmReturn(alpha - dx,beta))/ (2 * dx)
    partial_beta = (R.lmReturn(alpha,beta + dx) - R.lmReturn(alpha,beta - dx)) / (2 * dx)
    
    gradient0 = [partial_alpha, partial_beta]
    return gradient0 

def a(vector,dx):
    alpha =  vector[0]
    beta = vector[1]    
      
    partial_alpha = (R.lmReturn(alpha + dx,beta) - R.lmReturn(alpha - dx,beta))/ (2 * dx)
    partial_beta = (R.lmReturn(alpha,beta + dx) - R.lmReturn(alpha,beta - dx)) / (2 * dx)
    return (partial_alpha)**2+(partial_beta)**2

def gradient_ascent(vector,epochs,lr,dx):
    x = np.zeros([epochs+1,2])     
    x[0] = vector 
    print R.lmReturn(vector[0],vector[1])
    for i in range(epochs):
        v =np.array(derivative(vector,dx))*lr
        vector += v
        x[i+1] = vector
        
        print R.lmReturn(vector[0],vector[1]), a(vector,dx)
        if a(vector,dx) < 1e-8:
            break
            
        
    print x
        