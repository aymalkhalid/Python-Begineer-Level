#Implicit Conversion which is done automatically by python and to aviod data loss.

intNumber=1269
floatNumber=1270.1231
anyNo = intNumber + floatNumber

#Python converts small data type to large data type to avoid the loss of data type.
print ("AnyNO is of Type Class:",type(anyNo))
print ("Anyno is :",anyNo)

#Explicit Type Conversion is to convert the data type of an object to required data type.
#Also called type casting because the user casts (change) the data type of the objects.
#Syntax: (required_datatype) ( expression)
strNumber='1268'
strNumber = int (strNumber)
anyNo = intNumber + strNumber
print(anyNo)

#Key Points to Remember:
#Type Conversion is the conversion of object from one data type to another data type.
#Implicit Type Conversion is automatically performed by the Python interpreter.
#Python avoids the loss of data in Implicit Type Conversion.
#Explicit Type Conversion is also called Type Casting, the data types of object are converted using predefined function by user.
#In Type Casting loss of data may occur as we enforce the object to specific data type
