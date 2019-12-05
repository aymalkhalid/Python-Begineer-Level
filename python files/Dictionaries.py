# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 02:50:51 2019
A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values.
@author: Aymal KHALID
"""
Car = {"Model": "Reborn",
       "Manufacturer": "Honda",
       "Year":2018
       }
print (Car)
access = Car["Model"]  #Method 1
Car.get("Model") #Method 2
print (access)
Car ["Year"] = 2019
Car ["Model"] = "Reborn I_vtec"
print(Car)
for x in Car:                           #looping all at once
    print(x)
for x in Car:                           #Looping One by One
    print(Car[x])
for x,y in Car.items():                 #Looping both key & Items
    print (x,y)
if "Model" in Car:
    print("Yes the Key exsists in the DictionarY Model is :", access)
    
Car["HP"] = 750                          #Adding Items to Dictionary.                                                      
print(len(Car))                          #Print length of the dictionary.
#There are several methods to remove item with specified key name:-
Car.pop("HP")                   #Removes item if no argument passed removed the last item in dictionary.
#del Car["HP"]
print(Car)
#Copying a Dictionary
newCar = Car.copy()
# newCar = dic(Car)
newCar["Model"] = "Civic"
newCar["Year"] =  2001
print("Dictionary of New Car is:",newCar)