# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:52:25 2019

@author: Aymal KHALID
"""

import numpy as np
print("::: 2D MATRIX ::")
array2D = np.arange(50).reshape((10,5))
print(array2D)
print(":::Transpose of 2D MATRIX :::")
print(array2D.T)
print("::Dot Product of 2D MATRIX :::")
dotproduct=np.dot(array2D.T,array2D)
print(dotproduct)
print(":: 3D MATRIX::")
array3D = np.arange(50).reshape((2,5,5))
print("IN a Slice of 2 and 5 rows & 5 Columns")
print(array3D)
print(":::Transpose of 3D MATRIX :::")
print(array3D.T)
print(array3D.transpose((1,0,2)))
#print(":::Dot Product of 3D MATRIX :::")
#dotproduct=np.dot(array3D.T,array3D)
#print(dotproduct)
print("IN a Slice of 5 and 5 rows & 2 Columns")
array3D = np.arange(50).reshape((5,5,2))
print(array3D)
print(":::Transpose of 3D MATRIX :::")
print(array3D.T)
print(array3D.transpose((1,0,2)))
print(":::Dot Product of 3D MATRIX :::")
dotproduct=np.dot(array3D.T,array3D)
print(dotproduct)
array = np.array([[1,2,3]])
print(array)
print(array.swapaxes(1,0))