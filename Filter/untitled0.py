# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 22:02:56 2016

@author: Yulia PC
"""
from scipy import signal
i = 0
N = 1000

s = list()
while i<1000:
    s.append(i)
    i = i + 1


for t in range(0,N):
    s[t] = N+t