# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:20:02 2019

@author: Aymal KHALID
"""
class Car:
    __maxspeed = 0
    __name = ""
    hp=0
    def __init__(self,chasis,Number):  #This special function gets called whenever a new object of that class is instantiated.
        self.chasis=chasis
        self.__Number=Number
        self.__maxspeed=420
        self.__name="Self_Driving_Car"
        self.__chasisno()
        self.hp=34
    def drive(self):
        print("Wow,it's a self Driving Car And it's Speed is " +str(self.__maxspeed)+ " An accelarion of " +str(self.hp) )
    def __chasisno(self):
        print( self.chasis)
        print(self.__Number)
    def modification(self,speed,name,Number): #settermethod to change private variable
        self.__maxspeed=speed
        self.__name=name
        self.__Number=Number
        return self.__maxspeed,self.__name,self.__Number
    
redcar = Car("19-1234213-534",1269)
redcar.drive()
speed = int (input ("[Enter The speed  ]"))
name = str (input(["Enter Name of the Car  "]))
Number = str (input (["Enter The number for no Plate "]))
print(redcar.modification(name,Number,speed))
print(redcar.__class__.hp)    # it's zero 
print()