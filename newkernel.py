# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:33:40 2020

@author: omri
"""
import numpy as np


def KernelMul(a,kernel):
    c=np.zeros([a.shape[0]-2,a.shape[1]-2])
    
    for x in range(c.shape[0]):
        for y in range(c.shape[1]):
            c[x][y]=GetSumOfmul(kernel,a[x:x+3,y:y+3])
    return (c)
def GetSumOfmul(kernel,array):
    d=np.array(kernel*array)
    z=0
    for row in range(d.shape[0]):
        for tur in range(d.shape[1]):
            z+=d[row][tur]
    return (z)
a=np.random.rand(8,8)
for x in range(a.shape[0]):
    for y in range(a.shape[1]):
        a[x][y]=5*(a[x][y])
kernel=np.random.rand(3,3)
for x in range(kernel.shape[0]):
    for y in range(kernel.shape[1]):
        kernel[x][y]=5*(kernel[x][y])
t=KernelMul(a,kernel)
print(t)
while(t.shape[0]>=kernel.shape[0] and t.shape[1]>=kernel.shape[1]):   
    t=KernelMul(t,kernel)
    print (t)


