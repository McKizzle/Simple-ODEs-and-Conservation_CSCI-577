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
    sim_d = [np.array([None, None, None])]
    sim_d.append(np.array([t_0, v_0, x_0]))
    
    sim_d_e = [None]
    sim_d_e.append(harmonic_energy(x_0, v_0))
    
    sim_a = [np.array([None, None, None])]
    sim_a.append(np.array([t_0, harmonic_analytic_velocity(x_0, t_0), harmonic_analytic_position(x_0, t_0)]))
    
    sim_a_e = [None]
    sim_a_e.append(harmonic_energy(x_0, v_0))

    dt = 0.0006
    t_max = int( 5 * 2 * np.pi + 1) # only go out to five cycles. 
    dt_steps = int(t_max / dt) + 1
    for step in range(2, dt_steps):
        t = step * dt + t_0
        tp1 = np.array([t])
        #sim_d.append(np.append(tp1, ode.euler(harmonic_oscillator, sim_d[step - 1][1:3], dt, t)))
        #sim_d.append(np.append(tp1, ode.euler_richardson(harmonic_oscillator, sim_d[step - 1][1:3], dt, t)))
        #sim_d.append(np.append(tp1, ode.rung_kutta(harmonic_oscillator, sim_d[step - 1][1:3], dt, t)))
        sim_d.append(np.append(tp1, ode.predictor_corrector(harmonic_oscillator, sim_d[step - 1][1:3], dt, t, ode.rung_kutta, sim_d[step - 2][1:3])))
        sim_d_e.append(harmonic_energy(sim_d[step][2], sim_d[step][1]))
        sim_a.append(np.append(tp1, [harmonic_analytic_velocity(x_0, t), harmonic_analytic_position(x_0, t)]))
        sim_a_e.append(harmonic_energy(sim_a[step][2], sim_a[step][1])) 

    # Calclate the error at the fifth cycle. 
    t_fcyl = 5 * 2 * np.pi
    fcyl_x_d = sim_d[dt_steps - 1][2]
    fcyl_x_a = sim_a[dt_steps - 1][2]
    print "The error is: %0.2f%% percent" % (error_calc([fcyl_x_d, fcyl_x_a]) * 100)

    sim_d.pop(0)
    sim_d_e.pop(0)
    sim_a.pop(0)
    sim_a_e.pop(0)

    sim_d = np.array(sim_d)
    sim_a = np.array(sim_a)
    sim_d_plt, = plt.plot(sim_d[:,0], sim_d[:,2], "r")
    sim_dv_plt, = plt.plot(sim_d[:,0], sim_d[:,1], "g")
    sim_a_plt, = plt.plot(sim_a[:,0], sim_a[:,2], "b")
    plt.legend([sim_d_plt, sim_dv_plt, sim_a_plt], ['Body Position', 'Velocity', 'Body Position Analytical'])
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.show()

    # Plot the energies of the two systems. 
    sim_d_e_plt, = plt.plot(sim_d[:,0], sim_d_e, "r")
#    sim_a_e_plt, = plt.plot(sim_a[:,0], sim_a_e, "b")
#    plt.legend([sim_d_e_plt, sim_a_e_plt], ['Energy Euler', 'Energy Analytical'])
    plt.legend([sim_d_e_plt], ['Energy'])
    plt.show()

    # Calculate the diffence between the two systems.
    e_diff = abs(sim_d_e[len(sim_d_e) - 1] - harmonic_energy(harmonic_analytic_position(x_0, t_max), harmonic_analytic_velocity(x_0, t_max)))
    print "Energy difference is %0.2fJ" % e_diff

def error_calc(x): 
    x_max = max(x)
    x_min = min(x)
    return (max(x) - min(x))/max(x)

def harmonic_oscillator(x, t, k=1.0, m=1.0):
    return np.array([ -k * x[1] / m, x[0]])

def harmonic_analytic_position(x_0, t, k=1.0, m=1.0):
    return x_0 * np.cos((k/m)**0.5 * t)

def harmonic_analytic_velocity(x_0, t, k=1.0, m=1.0):
    return -0.5 * x_0 * np.sin((k/m)**0.5 * t)

def harmonic_energy(x, v, k=1.0, m=1.0):
    return 0.5 * (k * x**2 + m * v**2)

if __name__ == '__main__':
    main()



