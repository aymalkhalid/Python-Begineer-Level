# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:42:31 2019

@author: Aymal KHALID
"""
import datetime
variable = datetime.datetime.now()
print (variable)
#Date Output in different form.
print(variable.year)
print(variable.microsecond)
print("Week Name short Version :: Week Name Full Version")
print(variable.strftime("  %a"),("::::::::::::::::::::"),variable.strftime("%A"))
print("Weekday as a number 0-6 :: Day of month")
print(variable.strftime("     %w"),(":::::::::::::::::"),variable.strftime("%d"))

# Creating Date Objects
""" To create a date ,we can use the datetime() class Constructor of the datetime Module."""
#Requires 3 parameters Y,M,Day.
Variable = datetime.datetime(2021,9,30,23,12,59,23)
print("Till this Day i Will have my Degree",Variable)
