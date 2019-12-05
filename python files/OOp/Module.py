# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:41:53 2019

@author: Aymal KHALID
"""
"""Import a py File Naming a Module
You can name the module file whatever you like,
but it must have the file extension .py"""
import Moduling
#Use a Module
Moduling.Name("Angar")
Variable = Moduling.person["Country"]
print(Variable)

#Using Variables in Module
Variable = Moduling.person["age"]
print(Variable)
Variable = Moduling.person["name"]
print(Variable)

# Using Built in Module
import platform 
Variable = platform.system()
print (Variable)

# Re-naming a Module
import Moduling as ex
Variable = ex.person
print(Variable)

#Using the dir() Function
Variable = dir(Moduling)
print(Variable)

from Moduling import person
print(person["age"])

