# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 22:05:55 2016

@author: Yulia PC
"""

def test(func,arg):
    return func(func(arg))
def mult(x):
    return x*x
print (test(mult,2))


triple = lambda x:x*3
add = lambda x, y: x+y
print (add(triple(3),4))