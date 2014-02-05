#!/usr/bin/env python2.7 

import pylab as py
import matplotlib.pyplot as plt
import numpy as np
import ode as ode

""" Simulate a falling object. 

A simple python script that simulates a falling body and
 compares the energy. 

F = -mg
y(t) = -1/2 * g * t^2 + y_o

"""
def main():
    x0 , g0 = 10.0, -9.8
    state = [np.array([g0, x0])]

    # Run the simuation for 100 time steps
    dt = 0.01
    t_0 = 1
    t_m = 100
    for t in range(t_0, t_m):
        state.append(ode.euler(falling, state[t - 1], dt))

    print state

    return 0

""" Function produced from the 'coupling'
    x: A numpy array of two numbers. The array must be of the form [a, y]

    return: A numpy array of two numbers resulting from the internal equations..

    For now the function simply assumes the object has a mass of 1.
"""
def falling(x):
    return np.array([ x[0], x[1] ])


if __name__ == '__main__':
    main()


