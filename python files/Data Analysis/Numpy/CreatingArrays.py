# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:09:45 2019

@author: Aymal KHALID
"""

import numpy as np
mylist =[1,2,3,4]
myarray = np.array(mylist)
print("Type is ",type(myarray))
mylist2 = [11,22,33,44]
mylists = [mylist,mylist2]
myarray2= np.array(mylists)
print("Matrix Array",myarray2)
print("Rows::Column",myarray2.shape)
print("Data Type",myarray2.dtype)
# Special Zero Array
myZeroArray=np.zeros([2,3]) 
print("Special Array Zero",myZeroArray)
print("Rows::Column::",myZeroArray.shape)
print("Data Type",myZeroArray.dtype)
#Special Case Array is Array of 1's
my1Array=np.ones([5,4])
print("#Special Case Array is Array of 1's",my1Array)
#Special Case Array of Zero's
emptyArray = np.empty(5)
print("Empty Array is ::",emptyArray)
emptyArray = np.empty([0])
print("Empty Array is ::",emptyArray)
#Identity Array Always going to be multidimensional Matrix
IdentityMatrix=np.eye(5)
print("Identity Matrix ::",IdentityMatrix , sep="")
#Making An array by arange Method
Arrange=np.arange(5,100,5)
print("Arrange Array is::",Arrange)
Arrange=np.arange(5,10)
print("Arrange Array is::",Arrange)
Arrange=np.arange(5)
print("Arrange Array is::",Arrange)