# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:58:17 2019
The *self* parameter is a reference to the current instance of the class,
 and is used to access variables that belong to the class.
@author: Aymal KHALID
"""

class First:            #create Class
    def __init__(self,number,name,age,dob):  #constructor,self is neccessary 
        self.name=name
        self.age=age
        self.dob=dob
        self.number=number
        
    def Age(self): #function in class
        print("Age in hours:",end="::")
        return self.age*24*360+5
    def factorial(reference,number):            
        if number==0:
            return 1
        else:
            return (number*reference.factorial(number-1))
        
object1 = First(2,"Aymal",21,"04-05-1998")    #object creation
object2 = First(1," ",19 ," ")
del object2.number
del object2
print(object1.age)     #access the instance attributes
print(object1.name)
print(object1.dob)                       
print(object1.Age())
object1.number=int(input(["Enter The number For Factorial"]))
print("Factorial of a No is::",object1.factorial(object1.number))

class Canis:
    species = "Bull_Dog"        # class attribute
    def __init__(self,name,age): # instance attribute
        self.name=name
        self.age=age
    def bark(self):
        print("Bark Bark")
    def info(self):
        return (self.name + " is " +str(self.age)+ " Year's Old.")
                                                            # Must Write return if none is printed
    def birthday(self):
        self.age+=1
    def setBudday(self,buddy):
        self.buddy=buddy
        buddy.buddy=self
moti = Canis("Moti",7)      # instantiate the Dog class
ozzy = Canis("Ozzy",3)
print("These Dog are of Specie",moti.__class__.species,sep="__")       # access the class attributes
moti.setBudday(ozzy)       #moti buddy name is::
ozzy.setBudday(moti)       #ozzy buddy name is::
print(moti.buddy.name)
print(ozzy.buddy.name)
print(ozzy.buddy.info()) 
print(moti.buddy.info())
#This Class is Child Class inherited from Canis """
class Wolves(Canis):
    #pass keyword use it when you don't want to add any other properties or methods"""
    species = 'Wild'
    def __init__(self,name,age,Type):
        super().__init__(name,age)
        self.Type=Type                    #New Attribute added
        print("Wolves Moves in Pack")
#Additionally, we use super() function before __init__() method. 
#This is because we want to pull the content of __init__() method from the parent class into the child class
    def info(self):
        return(self.name + "is " + str(self.age) + " Year's Old and is " + str(self.Type) )
    def bark(self):
        return (", Also They don't bark at all..")
def Polymorphism(C):
    C.bark
Adalwolf =Wolves("Adalwolf ",10,"young")
print(Adalwolf.info(),Adalwolf.bark())
print(Polymorphism(Adalwolf))
Polymorphism(moti)
