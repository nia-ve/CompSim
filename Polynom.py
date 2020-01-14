
class Poly:

    def __init__(self,coeffs): 

       self.coeffs = coeffs

    def __str__ (self):   #built-in function in python, used for string representation of object.
        return(str(self.coeffs))

    def printPoly(self):
        #Display the polynomial.
        coefficents= 'List of coefficents:' + str(self.coeffs)
        print(coefficents)
        #Print the polynomial a0 + a1x + a2x^2 + ...
        #zeroth order
        s = 'P(x) = ' + str(self.coeffs[0])
        #first order
        s += " + " + str(self.coeffs[1]) + "x"
        #second order +
        for i in range (2, len(self.coeffs)):
            if self.coeffs[i]==0:
                s=s
            else:
               s += " + " +str(self.coeffs[i]) + "x^"+str(i)
        print (s)


    def order(self):
        order=len(self.coeffs)-1
        print("The order of this polynomial is " +str(order))


    def add(self,poly2):
        poly_sum = [self.coeffs[i] + poly2.coeffs[i] for i in range(len(self.coeffs))]

        return poly_sum