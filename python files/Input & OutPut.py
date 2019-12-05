#We can also import some specific attributes and functions only, using the from keyword.
from constant import Gravity
print (Gravity)
#We can also import the whole attributes and functions also.
import constant
print (constant.PI)
#print ( print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False))
print ( 'Aymal' ,'Nangial ', 'Arsalan ', ' ',sep='Khalid ,' , end= ' Are Siblings')

#Output Formatting str.format() method it's visible to any string object

rollno = 1269
rollno1 = 1270
print (' Aymal khalid Roll no is {} and nangial khalid is {} '.format(rollno,rollno1))
print('I love {0} and nangial loves {1}'.format('Everything','Choclates'))
print('I love {1} and nangial loves {0}'.format('Everything','Choclates'))

# we can even use keyword arguments to format the string.

print ('Hello {name}, {greeting}'.format (name = 'Aymal Khalid' , greeting = 'Have a good Day'))

# % can be used to accomplish Rounding off of NO's and to format Real No's

x= 1.99
print ("The Valuse of X is %1.2f" % x)
print ("The value of X is % 1.1f" %x)

#Python input To take input from the user the Syntax is input( [Enter your Message for the user] )
name = input (["Enter your Name"])
print ('Hello {name}, {greeting}'.format (name = name , greeting = 'Have a good Day'))
Number = int (input(["Enter Your Number"]))
print (Number,type(Number))
int (Number)
print (eval ('Number +1'))
