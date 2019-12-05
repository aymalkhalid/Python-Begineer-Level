# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 23:01:59 2019

@author: Aymal KHALID
"""
number =  float (input(["Enter You NUmber"]))
number1 = float (input(["Enter Your Number"]))
if number>number1:
    print("This Number {number} is greater".format(number=number))
elif number<number1: 
    print("This Number {number} is greater".format(number=number1))
else: 
    print ("The Numbers Are Equal {}==={}".format(number,number1))
if number > 0 :
    print ("Number is Positive")
elif number<0:
    print ("Number is Negative")
elif number==0:
    print ("NUmber is Zero")
else:
    print ("Number is not real")
if number >= number1 and number <= number1:
    print("Numbers are equal")
 
number2 = int (input("[Enter A Number]"))

if number2<10:
    while number2<10:
        number2 += 1          #This is the increment
        if number2==11:
           break    
        elif(number2<=9):     #don't print till it's 9 or less
           continue
        print(number2)
elif (number2==9):
        print ("number is equal to ===",number2)
 
string = "Aymalieo1u1"
for  vowels in string:
    if vowels == '1':
        print("Number Found")
        break
    elif vowels=='a' or vowels=='A' or vowels=='a' or vowels=='A' or vowels=='U' or vowels=='u' or vowels=='O' or vowels=='o' or vowels=='I' or vowels=='i' or vowels=='E' or vowels=='e': 
        print("The following are vowels in the string:" ,vowels)
for i in range(0,22,2):
    print(i)
else:
    print("Table upto 10 multiples finished")
    
colour = ['big','red','tasty']
fruit = ['apple', 'peach' , 'apricot']
for x in colour:
    for y in fruit:
        print("Adjancey is ::::",x,y)