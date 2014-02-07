# The ODE (ordinary differential equations) module contains eulers method.
import numpy as np

def euler(f, x, dt, t):
    return f(x, t) * dt + x

def euler_richardson(f, x, dt, t):
    return x + f(x + f(x, t) * dt / 2.0, t + dt / 2.0) * dt


