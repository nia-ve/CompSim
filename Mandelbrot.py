# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:40:06 2020

@author: s1787087
"""

import numpy as np
import matplotlib.pyplot as plt

# optimise code
from numba import jit

class Mandelbrot:
    
    def __init__(self, numx, numy, xmin, xmax, ymin, ymax, nmax, zmax, col):
        # num of points
        self.numx = numx
        self.numy = numy
        
        # region of complex plane
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        
        # upper iteration limit
        self.nmax = nmax
        
        # threshold value = |z|
        self.zmax = zmax
        # colour map
        self.col = col

    # check whether point in complex plane is in Mandelbrot set
    @jit
    def mandel(self, x, y):
        n = 0
        z = complex(x, y)
        c = z
        while (n < self.nmax):
            z = z*z + c
            if abs(z) > self.zmax:
                return n
            n +=1
        return n

    # generate and show mandelbrot set
    def run(self):     
        # create numpy arrays of pts in complex plane (or can use arange with incremements)
        X = np.linspace(self.xmin, self.xmax, self.numx)
        Y = np.linspace(self.ymin, self.ymax, self.numy)
 
        # create coordinate arrays
        XX, YY = np.meshgrid(X, Y)

        # vectorize mandel method
        vmandel = np.vectorize(self.mandel)

        # and call the vectorised method
        Z = vmandel(XX, YY)

        # plot the result
        plt.imshow(Z, cmap=self.col, extent = (X.min(), X.max(), Y.min(), Y.max()))
        plt.title('The Mandelbrot Set')
        plt.xlabel('Re(c)')
        plt.ylabel('Im(c)')
        plt.show()
    
        
