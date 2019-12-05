# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:10:22 2019

@author: Aymal KHALID
"""
#Method->1
class Iterator:
    def __iter__(self):            #must always return the iterator object itself.
        self.no=2
        return self
    def __next__(self):           #allows you to do operations, and must return the next item in the sequence.
        number=self.no
        self.no+=1
        return number

objects = Iterator()
myiterator = iter(objects)
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
# For Every new object the iterator Starts from beginning.
objects1 = Iterator()
seconditerator = iter (objects1)
print(next(seconditerator))

# Method->2 
# To Prevent Iteration from going forever:
class iterator:
    def __iter__(self):
        self.no=1
        return self
    def __next__(self):
        if self.no<=20:
            number=self.no
            self.no += 1
            return number
        else:
            raise StopIteration
myobject = iterator()
MyIterator = iter (myobject)
for i in MyIterator:
    print(i)            