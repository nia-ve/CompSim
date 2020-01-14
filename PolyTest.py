from Polynom import Poly

#to test Poly class (Checkpoint1)
#class PolyTest(object):

def main():

   coeffs1= [1,2,3,4,5]
   poly1= Poly(coeffs1)
   print('Polynomial 1:')
   poly1.printPoly()
   poly1.order()

   coeffs2=[2,2]
   poly2=Poly(coeffs2)
   print('Polynomial 2:')
   poly2.printPoly()

   coeffs3=[-3,-10, 0,1]
   poly3=Poly(coeffs3)
   print('Polynomial 3:')
   poly3.printPoly()

   print(coeffs1+coeffs2)

#poly1.add(poly2)
operation = input("Run test? (Y/N):")
if (operation == 'Y'):
        main()
else:
        print ("no")
