#Operators are special symbols in Python that carry out arithmetic or logical computation.
Number = int (input(["Enter your Number"]))
Number1 = int (input(["Enter your Number"]))
# I have to do this thing of having format and seprator in the same print)
print ( 'The number you Entered are {Number},{Number1}'.format( Number=Number , Number1=Number1), sep=' And ')
print ("Addition of the two number is :" , Number+Number1)
print ("Subtraction of the two number is. " , Number-Number1)
print("Division of the two number (/)which gives the Quotient is  :", Number/Number1)
print ("Division of the two number (%) which gives the Remainder:" , Number%Number1)
print ("Floor division that results into whole no (//):", Number//Number1)
Number = int (input(["Enter your Number"]))
Number1 = int (input(["Enter Raised to the Power"]))
print ("Raised to the power of NUmber is :", Number**Number1)
# Comparision operator
Number = int (input(["Enter your Left Operand"]))
Number1 = int (input(["Enter your Right Operand"]))
print ('Left < Right ::::' , Number<Number1)
print ('left > Right ::::' , Number > Number1)
print ('Left==Right::::', Number==Number1)
print ( 'left>=Right::::', Number>=Number1)
print ( 'left<=Right::::' , Number<=Number1)
#Logical Operators
Number = True
Number1 = False
print (" THe value of Number is {0} , And Number1 is {1} " .format ( 'True', 'False'))
print("Using the And Operator the Result is:" , Number and Number1)
print (" Using the Or Operator the Result is: " , Number or Number1)
print ("Using the not Operator the Result For Number is :" , not Number  )
#BitWise Operators Act on operands as if they were string of binary digits.It Operates bit by bit.
x = 10  #0000 1010 in binary
y =4     #0000 0100 in binary        
print ("Bitwise & Operator", x & y)
print ("BitWise | Or Operator",x | y)
print ("BitWise Not ~ Operator" , ~x)
#Rule 1 : If both bits are 1 then XOR’ed bit will be 0.
#Rule 2 : If both bits are 0 then XOR’ed bit will be 0.
#Rule 3 : If one bit is 0 and one bit is 1 XOR’ed bit will be 1.
print  ("Bitwise Xor Operator" , x^y)
#A bit shift moves each digit in a number's binary representation left or right.
#When shifting left, the most-significant bit is lost, and a 00 bit is inserted on the other end.
print ("Bitwise Left shift  1 times and 2 times" , x << 1 , x<<2 ,sep=',')
print ("Bitwise Right Shift 1 time and 2 times" , x>>1 , x>>2 , sep=',')
#Assingment Operators
x +=5
print("Value of x+=5 is:::: ",x)
x -=5
print ("Value of x-=5 is::::::",x)
x*=5
print ("Value of x*=5 is::::::",x)
x/=5
print ("Value of x/=5 is::::::",x)
x%=5
print("Value of x%=5 is ::::",x)
x//=5
print ("Value of x//=5 is :::::",x)
x**=5
print ("Value of X**=5 is::::",x)
y&=2
print ("Value of X&=5 is ::::", y)
y |= 2
print ("Value of X|=Y is ::::",y)
y^=2
print ("Value of X^=Y is :::::", y)
y>>=2
print ("Value of X>>=2 is :::::",y)
y<<=2
print ("Value of X<<=2 is :::::" , y)
#identity operators is and is not are used to check if two values are located
#in the same part of the memory.Two variables that are equal does not imply that they are identical.
x1 = 5
y1 = 4
x2 = 'Hello'
y2 = 'Hella'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
# Output: true
print(x2 is not y2)
# Output: True
print(x3 is y3)
# Output: False
#Membership operators in and not in are the membership operators in Python.
#They are used to test whether a value or variable is found in a sequence
#(string, list, tuple, set and dictionary).In a dictionary we can only test for presence of key,
#not the value.
x = 'Hello world'
y = {1:'a',2:'b'}
# Output: True
print('H' in x)
# Output: True
print('hello' not in x)
# Output: True
print(1 in y)
# Output: False
print('a' in y)
