import matplotlib.pyplot as plt
import scipy as scy
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

    # Method to check whether point in complex plane is in Mandelbrot set:
    def mandel(self, x, y):
        n = 0
        z = complex(x, y) #creates complex number x + yj
        c = z
        while (n < self.nmax):  #from 0-> max iterations ie 225
            z = z * z + c
            #print(z)
            if abs(z) > 2:
                return n
            n += 1
        return n


    # generate and show mandelbrot set
    def run(self):
        # create numpy arrays of pts in complex plane (or can use arange with incremements)
        X = np.linspace(self.xmin, self.xmax, self.numx)
        Y = np.linspace(self.ymin, self.ymax, self.numy)

        # create coordinate arrays
        XX, YY = np.meshgrid(X, Y)
       # print(XX)
        #plt.plot(XX, YY, marker='.', color='k', linestyle='none')
        #plt.show()

        vectorized_mandel = np.vectorize(self.mandel)
        #call vectorized method;
        Z = vectorized_mandel(XX, YY)  # number of iterations
        print(Z)

######### then plot::
        plt.imshow(Z, cmap=self.col, extent=(X.min(), X.max(), Y.min(), Y.max()))
        plt.title('The Mandelbrot Set')
        plt.xlabel('Re(c)')
        plt.ylabel('Im(c)')
        plt.show()


man = Mandelbrot(10, 10, -2.025, 0.600, -1.125, 1.125, 10, 'prism')
man.run()
