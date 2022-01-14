# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 23:07:20 2021

@author: ninht
"""

def f(x):
    return (x**3)-12*x

def f1(x):
    return (3*(x**2))-12

def f2(x):
    return 6*x

xi=3
eps=0.01

while True :
    xF=xi-f1(xi)/f2(xi)
    if (f1(xF)<eps):
        break
    xi=xF
    
print(xF)
    