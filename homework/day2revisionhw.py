name = "Today's Home work Python Data types"
print(name.center(20,"*"))

"""
Built in Data types

Text type -- string (str)
Numeric type ---int,float,complex
Sequence type---- list,tuple,range
Mapping type-----dict
set type -----set, frozenset
Boolean type -----bool
Binary types -----bytes,bytearray,memoryview

"""
# we can get data types by using type()
#int ex
number = 8
print(type(number))
#setting datatype ex
number= int (8)
print(type(number))
print("----------------------")
#string ex
x= "Hello GOOD morning"
print(x)
print(type(x))
#setting datatypeex
x = str("Hello GOOD morning")
print(type(x))
print("----------------------")
#Float ex
f= 10.5
print(f)
print(type(f))
#setting datatype ex
f = float(10.5)
print(type(f))
print("----------------------")

#complex ex
c = 1+2j
print(c)
print(type(c))
#setting datatype ex
c = complex(1+2j)
print(type(c))
print("---------------------")
#List ex
l = ["Milk", "cookies", "Fruits"]
print(l)
print(type(l))
#setting datatype ex
l = list (["Milk", "cookies", "Fruits"])
print(type(l))
print("------------------------")
# tuple ex
t = ("nuts","icecream","flowers")
print(t)
print(type(t))
#setting datatype ex
t = tuple(("nuts","icecream","flowers"))
print(type(t))
print("------------------------")
#range ex
r = range(8)
print(r)
print(type(r))
#setting datatype ex
r = range(8)
print(type(r))
print("------------------------")
#dictionary ex
d = {"name": "pen", "colour": "red"}
print(d)
print(type(d))
#settint datatype ex
d = dict({"name": "pen", "colour": "red"})
print(type(d))
print("------------------------")
#set ex
s = {"cricket","football","baseball"}
print(s)
print(type(s))
#setting datatype ex
s = set({"cricket","football","baseball"})
print(type(s))
print("------------------------")
#frozenset
fs = frozenset({"cricket","football","baseball"})
print(fs)
print(type(fs))
#setting datatype ex
fs = frozenset({"cricket","football","baseball"})
print("------------------------")

#boolean ex
b= True
print(b)
print(type(b))
#setting datatyoe ex
b = bool(5)
print(type(b))
print("------------------------")
#byte ex
by= b"hello"
print(by)
print(type(by))
#setting datatype ex
by = bytes(5)
print(type(by))
print("------------------------")
#bytearray ex
x = bytearray(5)
print(x)
print(type(x))
print("------------------------")
#memoryview ex
m= memoryview(bytes(3))
print(m)
print(type(m))
print("------------------------------------------------------------")
txt = "python Numbers"
print(txt.center(55,"*"))
# there are three numeric types in python
#int
#float
#complex
num1 = 1       #int
num2 = 5.6     #float
num3 = 1j      #complex
print(type(num1))
print(type(num2))
print(type(num3))
#int ex
num_1= 2
num_2 = 7655433445
num_3 = -987656
print(type(num_1))
print(type(num_2))
print(type(num_3))
"-----------------------"

#float ex
f_num1 = 1.78
f_num2 = 1.0
f_num3 = 35.87
print(type(f_num1))
print(type(f_num2))
print(type(f_num3))
#floats with scientific numbers
_fnum1 = 67e3
_fnum2 = 23E4
_fnum3 = -67.87E100
print(type(_fnum1))
print(type(_fnum2))
print(type(_fnum3))
"-------------------------"
#complex ex
com  = 2+3j
com1 = 5j
com2 = -5j
print(type(com))
print(type(com1))
print(type(com2))
print("--------------------------------------------------------------")
topic = "Convert from one type to another"
print(topic.center(55,"*"))
x = 2
y= 5.6
z = 1+2j
#convert int to float
a = float(x)
#convert float to int
b = int(y)
# convert into to complex
c = complex(x)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
#"we cannot convert complex into any other number"

#"Random number"
#Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers
#Import the random module, and display a random number between numbers
import random
print(random.randrange(1,15))
print("-------------------------------------------------------------------------------------")
Nexttopic =" Python Casting"
print(Nexttopic.center(55,'!'))
#Casting in python is therefore done using constructor functions:
#int() - constructs an integer number from an integer literal, a float literal
#(by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
#float() - constructs a float number from an integer literal, a float literal or a string literal
# (providing the string represents a float or an integer)
#str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
#INTEGERS
x = int(2)
y = int(4.5)
z= int('7')
print(x,y,z)
#FLOATS
f1 = float(2)
f2 = float(3.8)
f3 = float("8")
print(f1,f2,f3)
#STRINGS
s1 = str("l1")
s2 =str(2)
s3 = str(4.5)
print(s1,s2,s3)

#Type of conversion : The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion.

#Implicit Type Conversion
#Explicit Type Conversion
"""
In Implicit type conversion, Python automatically converts one data type to another data type. 
This process doesn't need any user involvement.

"""
# Example
num_int = 32
num_flo = 1.23
num_new = num_int+num_flo
print("datatype of num_int:" ,type(num_int))
print("datatype of num_flo:" , type(num_flo))
print("value of num_new: ", num_new)
print("datatype of num_new: ", type(num_new))
print("--------------------------------------------------------------")
"""
#EXAMPLE
num1_int = 25
num1_str = "44"
print("datatype of num1_int:", type(num1_int))
print("datatype of num1_str :", type(num1_str))
print(num1_int+num1_str)
"""
"""
We add two variables num_int and num_str.
As we can see from the output, we got TypeError. 
Python is not able to use Implicit Conversion in such conditions.
However, Python has a solution for these types of situations
which is known as Explicit Conversion.
"""
# EXPLICIT EXAMPLE
num1_int = 25
num1_str = "44"
print("datatype of num1_int:", type(num1_int))
print("datatype of num1_str before casting :", type(num1_str))
num1_str = int(num1_str)
print("datatype of num1_str after type casting: " , type(num1_str))
num_sum = num1_int + num1_str
print("sum of num1_int and num1_str:", num_sum)
print("datatype of the sum: ",type(num_sum))
print("--------------------------------------------------------------")






