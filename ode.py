# The ODE (ordinary differential equations) module contains eulers method.
import numpy as np

def euler(f, x, dt, t):
    return f(x, t) * dt + x

