#They have duplicate members:- starts from 0--------
#Ordered and Changable
thislist = ['Aymal' , 'Nangial' ,'Arsalan','Aymal']
#Ordered and unChangable
thistuple=('Aymal','Nangial','Arsalan','Aymal')

#They Don't have Duplicate members:-
#Unordered , Changeable , & Unidexed
thisSet={'Aymal','Nangial','Arsalan'}
thisdictionary={'1269','Aymal', '1269' , 'Nangial','1269','Arsalan'}

print(thislist)       #print entire list
print(thislist[1:2]) #print specific index or slice through
thislist[3]= "ValueChanges"
for x in thislist:     #looping through a list
    print(x)

if "aymal" in thislist:    #check if item in list
    print("Aymal is in this list")

print(thislist)
print(len(thislist)) #printingLengthofalist
thislist.append(1278) # Value to add at the end of the list.
thislist.insert(3,"Value Inserted") #Value inserted at indexed 3
print(thislist)
thislist.remove("Aymal") #to remove a specific item from
print(thislist)
thislist.pop(3) # removes specified index  or removes last value from a list
print(thislist)
del thislist[3]  #removes specified index by using del keyword
                        #can also del complete list
print(thislist)
thislist.clear()# Clear lists while 
print(thislist)
copylist=thislist.copy()  # Copying a list ,
print(copylist,"THis is list is copied")

#--------TupleThey have duplicate members:- starts from 0 ,Ordered and unChangable--------------------------------------

# Accessing Tuple.
print(thistuple[1])
#looping through Tuple.
for x in thistuple:
    print(thistuple)
#checking if item exsit
if "Aymal" in thistuple:
    print("Item Founded")#To find length of tuple
print(len(thistuple))
#can't change items but can delete the tuple entirely.
del thistuple
thistuple=tuple(("Anar","Saab","Anar"))    # Another way to assign tuple
print (thistuple)
count=thistuple.count('Anar')           #count a value in the tuple
print(count)
index=thistuple.index("Anar")
print (index)
#---------------------Set,They Don't have Duplicate members,nordered , Changeable , & Unidexed-------------------------------------
print(thisSet)

for x in thisSet:
    print ("Looping through Values",x)

if  "Aymal" in thisSet:
    print ("Value Founded")
thisSet.add("SingleValueAdded")  #to add one value
thisSet.update(["More","Than ONe Value Added"]) #to add more than one value
print(len(thisSet))
print("Nangial" in thisSet)             #Check if a value exsit by using keyword in
print(thisSet)
thisSet.remove("More")        #Changeable so can we remove a value.
thisSet.discard("SingleValueAdded") # remove using discard method it wont raise error if not there.
print("Value removed ",thisSet)
x=thisSet.pop() #pop removes the last item as its unindexed so we wont know which is last value.
print (x)
print (thisSet)
thisSet.clear()        #Clears the set or Empty's it.
print (thisSet)
copyThisSet=thisSet.copy() #copying a set

#Returns a set containing the difference between two or more sets
difference = copyThisSet.difference(thisSet)#Return a set that contains the items that only exist in set copyThisSet, and not in set thisset:
print("the Difference is:",difference)
fruits = {"apple", "banana", "cherry"}
product = {"google", "microsoft", "apple"}


#removes the items in this set that are also included in another specified set..
product.difference_update(fruits)
print ("Removes item which exsit in both set",product)
#intersection returns a set that contains  the similarity between two or more sets.
intersection = fruits.intersection(product)
print ("Intersection of 2 set is;." , intersection)
fruits.add("apple")
product.add("apple")
thisSet.add("apple")
#Removes the items in this set that are not present in other, specified set(s)
fruits.intersection_update(product,thisSet)
print("return a set with items that is present in all other set" , fruits)
alphabets={'a','b','c','d','e','i','o','u'}
vowels = {'a','e','i','o','u'}
subset=vowels.subset(alphabets)
print ("Subset is :", subset)
