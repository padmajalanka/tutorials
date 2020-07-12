print("HELLO WORLD!")


 # Indentation

'''
 This is Padmaja's First program comment
 comments in Python is # sign or " " or ''
'''


"""
 Number of spaces is important in same block of code.
 
"""
if 5 > 2:
    print("Five is greater than 2 !")

"""if 5 > 2:
    print("Five is greater than 2 !")               This will give indntation error.
         print("Five is greater than 2 !")
"""
if 5 > 2:
    print("Five is greater than 2 !")
    print("Five is greater than 2 !")

"""
  Variables
   Variables are containers storing data values.
   Pythoin has no command for declaring variables.
  Variables do not need to be declared with any type and they can change type after they have been set.
  
"""
x = 5
y = "john"
print(x)
print(y)

x =3
x= "John"
print(x)

# String variables can be declared either by using single or double quotes.

x="John"
# or
x='john'
print(x)

#a vriable must start with a letter or underscore character
#A variable name can't start with a number.
# Variable name can start with lpha- nummeric,characters and underscore.
# variable names are case sensitive.
myvar = "Padmaja"    # like myname = "padmaja"
my_var="Sudha"       # like my_ friend = "sudha"
_my_var="John"       # like _my_ friend name = "Kiran"
myvar="salley"
MYVAR= "John"
print(myvar)         # print(myname)
print(my_var)        # print(my_friend)
print(myvar)         # print( _my_Friend)
print(myvar, my_var,_my_var)
# multiple variables in one line
x, y, z = "Banana", "Orange", "Peach"
print(x)
print(y)
print(z)
print(x,y,z)
# same value to multiple variables
a=b=c = "Banana"
print(a)
print(b)         # give numerics to a,b,a or change numeric to a and put same as b,c
print(c)
a = "orange"
print(a)
print(b)
print(c)
# to combine both text and a variable python uses + character
#Day 2
x="awesome"
print("Python is " + x )
x="today we are learning continuation of previous day"
print( "Python is" + x)

x= "Python is "
y= "easy to learn"
z = x + y
print(z)
print(x +y)
print(x, y)

# for the numbers + work as a mathematical operator
x=5
y=5
print(x+y)
# if you try to combine number and string python gives N ERROR.
"""
x=5
y="John"
print(x+y)
"""

# Global variables : variables that are created outside of a function are global variables.

#global variables can be used by both inside the function and outside.

x= "easy to learn"
def myfun():
    print( "Python is " + x)
myfun()

x= "is this global value "
def fun():
    print("Vriables "+ x)
fun()
x= "call the function "
print("in python " + x)
def fun():
    x = "is this addition"
    print("in python " + x)
    if 5>2:
        print('5 is greater than 2')

fun()
print("in python " + x)



v1 = 14
v2 = 15
v3 = 16

def sum():
    print (v1 + v2 + v3)

def mult():
    print (v1 * v2* v3)

def subtr():
    print (v1 -v2 -v3)

sum()
mult()
subtr()
# once we define a function we have to call that after print.

#create a variable inside a function with the same name as Global variable.
x = "number one"
print ("Python is " + x)
def myfunc():
    x = "excellent"
    print("Python is " + x)
myfunc()

# To create a global variable inside a functionb .we can use global keyword.
def myfunc():
    global x
    x = "beautiful"
myfunc()
print("Python is " + x)

x = 1
def fun():
    global x
    x = "wow"
fun()
print("global variable is " + x)




# PYTHON DATATYPES
#VARIABLES CAN BE STORE DATA OF DIFFERENT TYPES.
#TEXT TYPE STRING EX:
x = "Hello Python"
print(x)
print(type(x))
# Integer Ex :
x=20
print(x)
print(type(x))
# Float Ex
x=10.5
print(x)
print(type(x))
# Complex Ex
x= 1+2j
print(x)
print(type(x))
#List Ex
x = ["Fruits","Vegitables", "spices"]
print(x)
print(type(x))
#Tuple Ex
x = ("lemon","Carrot","chillies")
print(x)
print(type(x))
# Range Ex
x= range (5)
print(x)
print(type(x))
x={"name" :"John" ,"Age": 25}
print(x)
print(type(x))

# Python casting
#specify variable types
#casting in python is done by constructors.
#int() : constructs integer
#float()
#str()
# Int()
x= int(1)
y= int(2.8)
z = int("4")
print(x,y,z)
print(x+z)
print(x*z)
print(x-z)

#float()
# str()
#string literals

#Strings are arrays
a = "hello,padmaja"
print(a[1])
print(a[7])

#slicing
x = "hello,Padmaja"     # , and spaces are also counts
print(x[2:6])
print(x[2:5])
print(x[2:9])

#negative indexing
#String length     #length will start from
print(len(x))
print("length of the string is  " ,len(x))
print("length of the string is " , + len(x))

#Methods of Strings
#Strip()
a=  "Hello World!"
b=   "hello world!  "
print(a.strip(),b.strip())

#lower,upper,replace Homework
#split()
a= "hello world"
print(a.split(","))
a= "My name is padmaja"
print(a.split(" "))
a= "hello , world abc"
print(a.split(","))
txt = "my sons name are viswanath and Sriram"
a = "sons" in txt
print(a)
a= " " in txt
b= ", "
print(a)
print(b)

#format() we can add numbers and strings by format()
#age = 36
#txt = "my name is Padmaja ,i am " + age
#print(txt)

# by format()
age = 35
txt = "my name is Padmaja , I am {}"
print(txt.format(age))

#escape character is by using \
print(txt.casefold())

txt.swapcase()
(txt.capitalize().format(age))

# Boolean values
print(10>9)
print(10==9)
print(10<9)

a= 20
b= 15
if b>a:
    print("b is grater than a")
else:
    print("b is not grater than a")

# evaluate values and
x =  ""
y = 0
print(bool(x))
print(bool(y))

def testing ():
  a = 10
  b = 20
  return_value = True
  if a > b:
     return_value = False
  else:
      return_value = True
  return return_value
firstvalue = bool(testing())
print(bool(firstvalue))












