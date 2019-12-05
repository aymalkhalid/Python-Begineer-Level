name = str (input( 'Enter Your name' ))
print ("id of Name is "  , id(name))
number = 1
print ( "Id of NUmber is " ,id (number)) 
number+= +1
print( number)
print ( "Id of NUmber is " ,id (number))
print ("id of 2 is" , id(2))
number1 = 1
print ("Id of number is : " , id(number1))
#This dynamic nature of name binding makes Python powerful;
#a name could refer to any type of object.
a = 5
a = ' Hello Angara'
a =[1,2,3]
a = {1 ,2 ,3 }
# Functions are object too
def printName():
    print ("StakeHolders")
a = printName()
#   
def outer_function():
    b = 20
    def inner_function():
        b = 30
        print('a =',b)

    inner_function()
    print('a =',b)
     
b = 10
outer_function()
print('b =',b)

def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10
outer_function()
print('a =',a)
