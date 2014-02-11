# The ODE (ordinary differential equations) module contains eulers method.
import numpy as np

def euler(f, x, dt, t):
    return f(x, t) * dt + x

def euler_richardson(f, x, dt, t):
    return x + f(x + f(x, t) * dt / 2.0, t + dt / 2.0) * dt

def rung_kutta(f, x, dt, t):
    k_1 = f(x, t) * dt
    k_2 = f(x + k_1 / 2.0, t + dt / 2.0) * dt
    k_3 = f(x + k_2 / 2.0, t + dt / 2.0) * dt
    k_4 = f(x + k_3 / 2.0, t + dt / 2.0) * dt

    return 0

