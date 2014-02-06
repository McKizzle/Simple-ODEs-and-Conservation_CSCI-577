#!/usr/bin/env python
import numpy as np
import pylab as py
import matplotlib.pyplot as plt
import ode as ode

""" Runs a harmonic simulator
   
   Uses the following formulas to simulate a harmonic simulator. 

   F = -kx
   x(t) = x_0 cos(\sqrt{\frac{k}{m}} t)

   Energy conservation is then checked with 

   E= \frac{1}{2} k x^2 + \frac{1}{2} m v^2
"""
def main():
    x_0 = 1.0 # starting position
    v_0 = 0.0 # starting velocity
    t_0 = 0.0
    sim_d = [np.array([t_0, v_0, x_0])]
    sim_a = [np.array([t_0, harm_analytic(x_0, t_0)])]

    dt = 0.1
    t_max = 35
    dt_steps = int(t_max / dt) + 1
    for step in range(1, dt_steps):
        t = step * dt + t_0
        tp1 = np.array([t])
        sim_d.append(np.append(tp1, ode.euler(harm_osc, sim_d[step - 1][1:3], dt, t)))
        sim_a.append(np.append(tp1, harm_analytic(x_0, t)))

    sim_d = np.array(sim_d)
    sim_a = np.array(sim_a)
    sim_d_plt, = plt.plot(sim_d[:,0], sim_d[:,2], "r")
    sim_a_plt, = plt.plot(sim_a[:,0], sim_a[:,1], "b")
    plt.legend([sim_d_plt, sim_a_plt], ['Body Position', 'Body Position Analytical'])
    plt.show()

def harm_osc(x, t, k=1.0, m=1.0):
    return np.array([ -m * x[1] / k, x[0]])

# Analytic function that returns the position of the object. 
def harm_analytic(x_0, t, k=1.0, m=1.0):
    return x_0 * np.cos((k/m)**0.5 * t)

# Analytic function the returns the velocity. 
def harm_analytic_velocity(x_0, t, k=1.0, m=1.0):
    return -0.5 * x_0 * np.sin((k/m)**0.5 * t)

if __name__ == '__main__':
    main()



