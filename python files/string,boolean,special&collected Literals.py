strings = "This is Aymal Khalid Yo!"
char = "A"
multilineString = """ I am here to learn Python and Excel my carrer in python
                      and data science """
unicode = u"\u00dcnic\u00f6de"
unicode2= u"\u0041\u00DD\u004D\u00C4\u00EE"  "And is encoded using escape chars" 
rawStr = r"raw \n string"
what = """an international encoding standard for use with different languages and scripts, by which each letter, digit, or symbol is assigned a unique numeric value that
                applies across different platforms and programs"""
print (strings)
print (char)
print (multilineString)
print (unicode)
print (rawStr)
print (unicode2 , what)
#Boolean litearl
boolean = (1 == True )
boolean2 = (0 == False)
a = True +4
b = False + 9

print ("Boolean is " , boolean)
print ("Boolean2 is " , boolean2)
print  ("a is " , a)
print  ("b is " , b)

#Python contains one special literal i.e.None.
#We use it to specify to that field that is not created.

drink = "Available"
food = None
def menu (x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

fruit = ['Mango','Apple']
numbers = (1,2,3)
dictionary = {'a':'Apple', 'b': 'Ball' , 'C' : 'Cat' }
vowels = {'a','e','i','o','u'}

print(fruit)
print(numbers)
print(dictionary[0:1])
print(vowels)
