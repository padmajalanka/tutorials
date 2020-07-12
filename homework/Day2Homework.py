# Today we learned Global variabl,Local variabl,Global Keyword
# also learned about data types.
x= "Very Hot and cloudy"
def Weather():
    print("Today's weather is " + x )
Weather()

x = "Very Hot"
def Temperature():
    x ="Wear Hat and cooling Glasses when you go out"
    print("today's weather is hot " + x)
Temperature()

x = "Very Hot"
print("Weather is " + x )
def Temperature():
    x ="Wear Hat and cooling Glasses when you go out"
    print("today's weather is hot " + x)
Temperature()

#Global Keyword
def shopping():
    global x
    x = "Get Milk and Fruits"
    print("when you go for shopping " + x)
shopping()

#  DataTypes
#Type() function
x= "wow"                    # string
print(type(x))

#setting datatypes Ex
a="Its cold inside"
print(type(a))

b = 5
print(type(b))

x= 1.
print(type(x))

y= 2j
print(type(y))

z = ["cloths" , "groceries" , "Vegitables"]
print(type(z))

a= ("Cerials" , "Coffee Powder" , "sugar")
print(type(a))

b= range(8)
print(type(b))

x = {"language" : "english" ,"Course": "Python"}
print(x)
print(type(x))

y = {"year" , "Months", "days"}
print(type(y))

x = frozenset  ({"selenium" , "Python", "qtp"})   # display x
print(x)
print(type(x))

z = True
print(z)     # display z
print(type(z))

a = b"Hello"
print(a)
print(type(a))

x=  bytearray(4)
print(x)
print(type(x))

y = memoryview(bytes(3))
print(y)
print(type(y))

# python Numbers
#Integers
x= 5
y= 2.5
z=  3j
print(type(x))
print(type(y))
print(type(z))

# integers
a = 8
b = 5678998
c = -2345
print(type(a))
print(type(b))
print(type(c))

#Float
x = 1.20
y = 1.2
z= - 2.234
print(type(x))
print(type(y))
print(type(z))

x = 26e3
y = 12e10
z = -12.85e100
print(type(x))
print(type(y))
print(type(z))

# Complex

a = 1+2j
b = 3j
c = -4j
print(type(a))
print(type(b))
print(type(c))

# Type Convwersion
x = 10
y = 1.5
z = 1+2j
#convert int to float
a = float(x)

#convert float into int
b= int(y)

# convert  int to complex
c = complex(x)

print(a)
print(b)
print(c)


print(type(a))
print(type(a))
print(type(a))

# we can't convert complex into any number.

#Random Number ; Python doesn'e have a random().we have to import random module
import random
print(random.randrange(1,8))