# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 02:44:11 2021

@author: ninht
"""
def f(i,s):
    return x(i,s)**2 - 1.5 * x(i,s)

def x(i,s):
    if i > 0:
        return x1 + (i - 1) * s
    else:
        return x1 + (i + 1) * s

def pasVA():
    s = 0.05
    i = 1
    if f(2,s) < f(1,s) :
        while f(i+1,s) < f(i,s): 
            i+=1
            s=2*s
        xa = x(i-1,s)
    if f(2,s) > f(1,s):
        while f(i+1,s) > f(i,s):
            i-=1
            s=2*s
        xa = x(i-1,s)
    elif f(2,s) == f(3,s):
        xa = x(1,s)
    elif f(2,s) > f(1,s) and f(-2,s) > f(1,s):
        xa = x(-2,s)
    return xa

x1=0.0
r=pasVA()
print("Le point x* ~= ",r," est l\'optimum ")

