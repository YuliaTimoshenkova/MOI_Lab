"""
Kalman filter
"""
import random
import numpy
import pylab

N = 50
empty = (N,)
Signal = list()
i=0
while i<N:
    Signal.append(i)
    i = i + 1
for t in range(0,N):
   Signal[t] = (numpy.sin(2.0*numpy.pi) + numpy.sin(2.0*numpy.pi)) + 0.01*random.random()

process_variance = 1e-5
posteri_estimate = numpy.zeros(empty)
posteri_error_estimate = numpy.zeros(empty)
priori_estimate = numpy.zeros(empty)
priori_error_estimate = numpy.zeros(empty)
blending_factor = numpy.zeros(empty)

estimated_measurement_variance = 0.1 ** 2

posteri_estimate[0] = 0.0
posteri_error_estimate[0] = 1.0

for iteration in range(1, N):
    priori_estimate[iteration] = posteri_estimate[iteration - 1]
    priori_error_estimate[iteration] = posteri_error_estimate[iteration - 1] + 1e-5 
    blending_factor[iteration] = priori_error_estimate[iteration] / (priori_error_estimate[iteration] + estimated_measurement_variance)
    posteri_estimate[iteration] = priori_estimate[iteration] + blending_factor[iteration] * (Signal[iteration] - priori_estimate[iteration])
    posteri_error_estimate[iteration] = (1 - blending_factor[iteration]) * priori_error_estimate[iteration]

pylab.plot(Signal, '--k')
pylab.plot(posteri_estimate, 'b')
pylab.xlabel('Iteration')
pylab.ylabel('Voltage')