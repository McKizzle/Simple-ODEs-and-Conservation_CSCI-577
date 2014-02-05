# The ODE (ordinary differential equations) module contains eulers method.
import numpy as np

def euler(f, x, dt):
    return f(x) * dt + x

