# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:02:51 2020

@author: omri
"""
import numpy as np
def Checkifmatsaregood(x,y):#checks if the mats have equal toorim in each row like if the mat is not a=[[1,2],[1,24,3],[1,32,4,2]]
    if(len(x.shape)==1 or len(y.shape)==1):
        return False 
    else:
        return True

def MathMult(x,y):
    if(Checkifmatsaregood(x,y)==False):
        return False
    k=(max(x.shape[0],y.shape[0]))
    t=(min(x.shape[1],y.shape[1]))
    z=np.zeros((k,t))
    if(x.shape[1]!=y.shape[0]):#if the matrix wont be as it needs to be the function will return a matrix full of zeros
        return z
    for i in range(x.shape[0]):
        for q in range(y.shape[1]):
            for t in range(y.shape[0]):
                z[i][q]+=x[i][t]*y[t][q]          
    return z


def Minmat(x,y):
    if(Checkifmatsaregood(x,y)==False):
        return False
    k=(min(x.shape[0],y.shape[0]))
    t=(min(x.shape[1],y.shape[1]))
    z=np.zeros((k,t))
    for i in range(k):
        for q in range(t):
            z[i][q]=(x[i][q])+(y[i][q])
    return (z)

def Maxmat(x,y):
    if(Checkifmatsaregood(x,y)==False):
        return False
    k=(max(x.shape[0],y.shape[0]))
    t=(max(x.shape[1],y.shape[1]))
    z=np.zeros((k,t))    
    for i in range(x.shape[0]):
         for t in range(x.shape[1]):
             z[i][t]+=x[i][t]
    for i in range(y.shape[0]):
         for t in range(y.shape[1]):
             z[i][t]+=y[i][t]
    return(z)       


x=np.array([[1,3,2],[4,5,6],[2,1,5],[1,2,3]])
y=np.array([[6,21],[1,6],[1,2]])
print (MathMult(x,y))
print (Minmat(x,y))
print (Maxmat(x,y))