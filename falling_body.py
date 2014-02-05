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
    t_0 = 0
    y_0 = 10.0 # m
    v_0 = 0.0  # m/s
    sim_d = [np.array([t_0, v_0, y_0])]
    sim_a = [np.array([t_0, fall_analytic(t_0, -9.8, y_0)])]

    print sim_a

    #print state
    #print state[0]
    #print state[0][1:3]

    # Run the simuation for two seconds.
    dt = 0.01 # step size
    t_max = 2 # maximum number of seconds to run. 
    dt_steps = int(t_max / dt) #number of dt increments to perform
    for t in range(1, dt_steps + 1):
        tp1 = np.array([t * dt + t_0])
        sim_d.append(np.append(tp1, ode.euler(fall, sim_d[t - 1][1:3], dt)))

    # Run the analytic solution to check the simulation.
    sim_a = np.array([t_0, fall_analytic(t_0, -9.8, y_0)
    

    #plot the falling object now.
    state = np.array(state)
    plt.plot(state[:,0], state[:,1], "r")
    plt.plot(state[:,0], state[:,2], "b")
    print state.shape
    plt.show()

    return 0


""" Function produced from the 'coupling'
    x: A numpy array of two numbers. The array must be of the form [a, y]

    return: A numpy array of two numbers resulting from the internal equations..

    For now the function simply assumes the object has a mass of 1.
"""
def fall(x, g=-9.8):
    return np.array([ g , x[0] ])

def fall_analytic(t, g, y_0):
    return -0.5 * g * t**2 + y_0


if __name__ == '__main__':
    main()


