# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 20:54:00 2019
Lambda functions are used when you need a function for a short period of time.
 This is commonly used when you want to pass a function as an 
                 argument to higher-order functions,
 that is, functions that take other functions as their arguments.
@author: Aymal KHALID
"""

def table(number,multiple): #printing a table 
    if multiple>9:
        return 0
    else:
      multiple+=1
      print( number * multiple)
      table(number,multiple)   #recursive call
print (table(2,0))

def square(number): 
    return number*number
print(square(3))
def factorial(number):
    if number==0:
        return 1
    else:
         return (number * factorial(number-1))
print(factorial(2))

""" A lambda function is a small anonymous function
which can take a no of arguments, but can only have 1 expression
Lambda arguments : Expression"""
square = lambda a:a**a
print("Square of 2 is:",square(2))
multiplication = lambda  a, b: a*b
print("Multiplication oF ",multiplication(2,3))
add = lambda a,b:a+b
print("Addition::",add(2,2))
sub = lambda a,b: a-b
print("Subtraction::",sub(2,2))

def testfunc(num):
    return lambda x : x * num  #x=result1(9)

result1 = testfunc(10)
result2 = testfunc(1000)

print(result1(9))
print(result2(9))

def myfunc(n):
  return lambda a : a - n         #a=11

double = myfunc(2)
tripled = myfunc(3)

print(double(11)) 
print(tripled(11))























