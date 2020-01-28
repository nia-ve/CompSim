from Mandelbrot import Mandelbrot

class MandelbrotTest(object):

    def run(self):               
        """
        Code to run mandelbrot
        """
# def __init__(self, numx, numy, xmin, xmax, ymin, ymax, nmax, zmax, col): 
        man = Mandelbrot(512, 512, -2.025, 0.600, -1.125, 1.125, 255, 2, 'prism')
        print(man.xmin)
        man.run()


m = MandelbrotTest()
m.run()
