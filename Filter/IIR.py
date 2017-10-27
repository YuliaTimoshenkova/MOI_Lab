"""
Buterworth filter 2
"""
import numpy as np
import matplotlib.pyplot as pl
import random

i = 0
N = Fs = 800
Fc = N / 4
T = 1.0 / Fs
Signal = list()
Filter = list()
freq = N / 10
while i < N:
    Signal.append(i)
    Filter.append(i)
    i = i + 1
for t in range(0,N):
    Signal[t] = (np.sin(2.0 * np.pi * freq * t / Fs) + np.sin(2.0 * np.pi * freq * t / Fs) / 3.0) / 2.0  + random.random()
 
alpha = (T * np.pi * Fc - 1) / (T * np.pi * Fc + 1)
for i in range(2, N):
    Filter[i] = pow((1 + alpha) / 2,2) * (Signal[i] + 2 * Signal[i - 1] +
    Signal[i - 2]) - 2 * alpha * Filter[i - 1] - pow(alpha , 2) * Filter[i - 2]
pl.clf()
pl.xlabel("Time")
pl.ylabel("Sample value")
pl.plot(Signal,'-g')
pl.plot(Filter, '--k')