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

    return x + (1.0/6.0) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)

def predictor_corrector(f, x, dt, t, bootstrap_func, x_nm1):
    """ Predictor Corrector method. 
        
        Unlike the other methods this function needs a bootstrap
        function to get started. This bootstrap function will only
        be used when x_nm1 is None

        The bootstrap function must be either;
            - euler
            - euler_richardson
            - rung_kutta
    """
    if not x_nm1[0]:
        x_nm1 = bootstrap_func(f, x, dt, t)
    
    return x + (1.0/2.0) * (f(x_nm1, t) + f(x, t))* dt 

