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
    sim_d = [np.array([t_0, v_0, y_0])] #t,v,x
    sim_d_energy = [fall_energy(y_0, v_0)]
    sim_a = [np.array([t_0, fall_analytic_velocity(t_0), fall_analytic(t_0, y_0)])] # t,v,x
    sim_a_energy = [fall_energy(fall_analytic(t_0, y_0), fall_analytic_velocity(t_0))]
    
    #print sim_d
    #print sim_d[0]
    #print sim_d[0][1:3]

    # Run the simuation for about two seconds.
    dt = 0.05 # step size
    t_max = 1.5 # maximum number of seconds to run. 
    dt_steps = int(t_max / dt) #number of dt increments to perform
    y_p = 10
    for step in range(1, dt_steps + 1):
        t = step * dt + t_0
        tp1 = np.array([t])
        sim_d.append(np.append(tp1, ode.euler(fall, sim_d[step - 1][1:3], dt, t)))
        sim_d_energy.append(fall_energy(sim_d[step][2], sim_d[step][1]))
        sim_a.append(np.append(tp1, [fall_analytic_velocity(t), fall_analytic(t, y_0)]))
        sim_a_energy.append(fall_energy(sim_a[step][2], sim_a[step][1]))
        

    #Plot the falling objects. Euler vs Analytical functions.
    sim_d = np.array(sim_d)
    sim_a = np.array(sim_a)
    y, = plt.plot(sim_d[:,0], sim_d[:,2], "r")
    y_anal, = plt.plot(sim_a[:,0], sim_a[:,2], "b")
    plt.legend([y, y_anal], ["Height", "Analytical Height"])
    plt.title("Position Comparison of the Analytical and Euler Systems")
    plt.xlabel("Time (sec)")
    plt.ylabel("Height (m)")
    plt.show()

    #Plot the energies of the two curves.
    e_plot_d, = plt.plot(sim_d[:,0], sim_d_energy, "r")
    e_plot_a, = plt.plot(sim_a[:,0], sim_a_energy, "b")
    plt.legend([e_plot_d, e_plot_a], ["Energy in discrete simulation", "Energy in analytical simulation"])
    plt.title("Energy Comparison of the Analytical and Euler Systems")
    plt.xlabel("Time (sec)")
    plt.ylabel("Energy")
    plt.ylim([97, 102])
    plt.show()

    #Calculate the energy difference
    e_diff = abs(sim_a_energy[len(sim_a_energy) - 1] - sim_d_energy[len(sim_d_energy) - 1])
    print "Energy difference is %0.2fJ" % e_diff

    return 0


""" Function produced from the 'coupling'
    x: A numpy array of two numbers. The array must be of the form [a, y]

    return: A numpy array of two numbers resulting from the internal equations..

    For now the function simply assumes the object has a mass of 1.
"""
def fall(x, t, g = -9.8): 
    return np.array([ g , x[0] ])

def fall_analytic(t, y_0, g=9.8):
    return -0.5 * g * t**2 + y_0

def fall_analytic_velocity(t, g=9.8):
    return -g * t

def fall_energy(x, v, g=9.8, m=1.0):
    return m * g * x + 0.5 * m * v**2


if __name__ == '__main__':
    main()


