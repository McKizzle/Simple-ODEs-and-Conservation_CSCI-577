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
    x_0 = 1 # starting position
    v_0 = 0 # starting velocity
    k = 1 # Spring constant
    m = 1 # Mass of the particle



    print 'running harmonic simulator'

def harm(x, t):


if __name__ == '__main__':
    main()



