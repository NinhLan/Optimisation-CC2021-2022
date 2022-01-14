# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 23:43:58 2021

@author: ninht
"""

def f(x):
    return x**3-x-1


def f1(x):
    return (f(x+dx)-f(x-dx))/(2*dx)

def f2(x):
    return (f(x+dx)-2*f(x)+f(x-dx))/((dx)**2)

xi=1
dx=0.01
eps=0.001

while True :
    xF=xi-f1(xi)/f2(xi)
    if (f1(xF)<eps):
        break
    xi=xF
    
print(xF)