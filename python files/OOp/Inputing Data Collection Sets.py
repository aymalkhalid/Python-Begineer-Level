# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:45:39 2019
 Inputing Collection data Types from User.
@author: Aymal KHALID
"""
#They have duplicate members:- starts from 0--------
#       Method # 1 
input_string = input ("Enter a list seprated by spaces")
list = input_string.split()
print ("Calculate sum of the list::")
sum = 0
print ("items in the list are::",list)
for num in list:
    sum += int(num)
print("Sum of the list is::",sum)

# Method #2
numbers =[]             #Ordered and Changable
maximum = int(input("Enter Maximum No You want to add in list::"))
for i in range(0,maximum):
     element=int(input("Enter Elements One by One"))
     numbers.append(element)
print (numbers)

fruits=[]                   #Ordered and Changable  
maximum = int(input("Enter the maximum no of Fruits you want to add::"))
for i in range(0,maximum):
    element= str(input("Enter Your favourite Fruits::"))
    fruits.append(element)
print (fruits)

#Ordered and unChangable

prayers = []
maximum = int (input("Enter the Maximum No for tuple"))
for i in range(0,maximum):
    element=str(input("Enter the Prayer You have offered Till now::"))
    prayers.append(element)
prayers = tuple(prayers)
print(prayers,type(prayers))

#---------------------Set,They Don't have Duplicate members,nordered , Changeable , & Unidexed-------------------------------------
prayers_set = []
maximum = int (input("Enter the Maximum No for tuple"))
for i in range(0,maximum):
    element=str(input("Enter the Prayer You have offered Till now::"))
    prayers_set.append(element)
prayers_set= set(prayers_set)
print(prayers_set,type(prayers_set))

#_____________________A dictionary is a collection which is unordered, changeable and indexed In Python dictionaries are written with curly brackets, and they have keys and values.
my_dict = dict()
 
key = input("Enter the key: ")
value = input("Enter the value: ")
my_dict[key] = value
print(my_dict)

Student = {}
maximum = int (input("Enter the Maximum"))
for i in range(0,maximum):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    Student[key]=value
print(":::",Student)
    