# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:11:04 2020

@author: s1787087
"""
import matplotlib.pyplot as plt

import numpy as np

class Mandelbrot:
    
    def __init__(self, numx, numy, xmin, xmax, ymin, ymax, nmax, col):
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

        # colour map
        self.col = col


# check whether point in complex plane is in Mandelbrot set:
    def mandel(self, x, y):
        n = 0
        z = complex(x, y)
        c = z
        while (n < self.nmax):
            z = z*z + c
            if abs(z) > 2:
                return n
            n +=1
        return n
        print(n)
      
    # generate and show mandelbrot set
    def run(self):     
        # create numpy arrays of pts in complex plane (or can use arange with incremements)
        X = np.linspace(self.xmin, self.xmax, self.numx)
        Y = np.linspace(self.ymin, self.ymax, self.numy)
 
        # create coordinate arrays
        XX, YY = np.meshgrid(X, Y)
        print(XX)
        plt.plot(XX, YY, marker='.', color='k', linestyle='none')


        yy, xx = np.mgrid[-5:6, -5:6]
        plt.figure()

        plt.grid()
        plt.xticks(xx[0])
        plt.yticks(yy[:, 0])
        plt.scatter(XX, YY, color="red", marker="x")



man = Mandelbrot(10, 10, -2.025, 0.600, -1.125, 1.125, 255, 'prism')
man.run()
