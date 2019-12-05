# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:22:35 2019

@author: Aymal KHALID
"""

import numpy as np
array = np.arange(0,11)
print(array)
#A value at index
print(array[2])
#Range
print(array[1:5])
print(array[0:5])
#Equaling the array to a value
array[0:6] = 100
print(array)
#reseting an array
array = np.arange(0,11)
sliceOfArray = array[0:5]
print("Slice OF an array",sliceOfArray)
#this Line below doesn't makes all the array to 99 but only upto index 5
sliceOfArray[:] = 99
#Effects the orignal array BECAREFUL!!!!!
print(sliceOfArray)
#python doesn't make's new copy's of the array it just 
print(array)
copyArray = array.copy()
print(copyArray)
#indexing in a 2d array
array2D = np.array([[5,10,15],[20,25,30],[35,40,45]])
print("2D Array is as::",array2D)
print("1 row ::",array2D[0])
print("2 row ::",array2D[1])
print("3 row ::",array2D[2])
print("Indivual Element::",array2D[0][1])
# row,column 
print("till second row but only first column",array2D[:2,0:1]) #till second row but only first column
print("till third row but only Second column",array2D[:3,1:2]) #till third row but only Second column
print("till third row but only third column",array2D[:3,2:3])  #till third row but only third column
print("third row last element",array2D[2:3,2])
#Fancy Indexing
arry2D = np.zeros((10,10))
print(arry2D)
length=arry2D.shape[1]
print(length)
for i in range(length):
    arry2D[i]=i
print(arry2D)
#Fancy Indexing 
print("Fancy",arry2D[[2,3,4,5]],arry2D[2:4])