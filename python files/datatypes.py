number = 1+2j
print (number,'Number is ',type(number))
print (number,'is a complex Number = ',isinstance(number , complex))
number = 'nangial'
print (number,'is a string = ',isinstance(number,int))
#slice operator can be used in both list & tuples but cant change value in tuple.

print ('l' not in 'nangial') # not in , n are membership operators which can only be used in strings
print ('i' in 'nangial')
items = [ 1, 2.33444, 1+2j,' nangial' ] #lists
#All the items in a list do not need to be of the same type.
print (items[0:4])
print ('items', items[0:2])
print ('items',items[-3])
items[1]='Khalid Khan'
print('list are mutable which means they can change:',items)
tuple = ({items})   #conversion from list to tuple.
list = ([items])    #conversion from tuple to list.
#tuple are immutable used to write protected data faster than list.

tuples=(1,2.444444423,333334241521534534,'nangial')
print ('tuple is :',tuples[2])

#strings are immutable represented using single or double quotes, """ are used to represent multiline strings
string = """ String is sequence of Unicode characters
We can use single quotes or double quotes to represent strings
Multi-line strings can be denoted using triple quotes, ''' or ""
Like list and tuple, slicing operator [ ] can be used with string.
Strings are immutable. """
print (string[0:60])

#Set is an unordered collection of unique items. Set is defined by
#values separated by comma inside braces { }. Items in a set are not ordered.
#We can perform set operations like union, intersection on two sets.
#Set have unique values. They eliminate duplicates.

Set = {1,2,45,6,3,1,56,63,2+3j,12.332}
print ( 'Set is as follow:' , Set)

#Dictionary is an unordered collection of key_value pairs,Used for huge amount of data.
#Optimized for retrieving data. Must know the key to retrieve the value.
#Key:value {}

Dictionary = {1268:'Arsalan',1269:'Aymal',1270 : 'Nangial'}

print(type(Dictionary))
print (Dictionary[1269])
