# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:23:17 2019

@author: Aymal KHALID
"""
fruits =[]             # list
maximum = int (input(["Enter the maximum no ::"]))
for i in range(0,maximum):
    element =str(input(["Enter the Values one by one"]))
    fruits.append(element)
fruits = tuple(fruits)   #Converting from List to Tuple
print(fruits)
print(type(fruits))

# Iterating through a Tuple
#Method->1
for i in fruits:
    print(i)
#Method ->2
myiterator= iter(fruits) 
for i in range(0,maximum):
    print(next(myiterator))

# Iterating through a string
    #Method->1
mystring = "Meme"
for i in mystring:
    print(i)
    #Method->2     Draw Back With this Method is That you have to determine the end by itself.
myiterator = iter(mystring)
print(next(myiterator)) 
print(next(myiterator)) 
print(next(myiterator)) 
print(next(myiterator))    