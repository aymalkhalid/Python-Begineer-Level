# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 00:22:04 2019

@author: Aymal KHALID
"""

def function():
    print("My first function")
function()

name = str(input(["Enter your name"]))

def function1(name):
    print ('Hello {name}, {greeting}'.format (name = name , greeting = 'Have a good Day'))
function1(name)

greetings = str(input(["Enter Greetings"]))

def greeting(name,greetings = "hooraah"): # If a parameter isn't passed it's default value is called.
    print('Hey, {name} , {greetings}'.format(name=name,greetings=greetings))

greeting(name,greetings)

food = ['Kufta','Donuts','CreamRoll']
def foodie(food):
    for x in food:
        print(x)
foodie(food)


