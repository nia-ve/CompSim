# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("hello")
 
class Snake:
  pass
 
snake = Snake()
name = "python" # set an attribute `name` of the class
print(snake)


class MyClass:
  x = 5
  
  
p1 = MyClass()  #object p1
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i


# suppose our target equation reads
#f(x)=105(x−0.9)2(x−1.1)3=0.

from classes import Derivative
from Newton import Newton
def f(x):
         return 100000*(x - 0.9)**2 * (x - 1.1)**3

df = Derivative(f)
Newton(f, 1.01, df, epsilon=1E-5)
