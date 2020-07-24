print("&&&&&&&&&&&&&&&&&&&Functions&&&&&&&&&&&&")
# or
topic = "functions"
print(topic.center(55, '$'))


def my_name():
    print("Hello my name is Padmaja")


my_name()

#function with arguments
def my_name(firstname):
    print(firstname + "lanka")

my_name("Raju")
my_name("Padmaja")
my_name("Viswanath")
my_name("Sriram")

##Python Builtin functions
#absolute function :returns absolute value of the specified number.
#SYNTAX is abs(n)
x = abs(3+5j)
print(x)
x = abs(-7)
print(x)
x = abs(-10.5)
print(x)

###all()
# the all() function returns true if all items in an iterable are true
# otherwise it returns false.
#if iterable item is empty it returns true.
mylist = [True,True,True]
print(all(mylist))

#ascii()
normaltext = 'Python is interesting'
print(ascii(normaltext))
othertext = 'python is interesting'
print(ascii(othertext))
###enumerate() function takes a collection and returns enumerate object
#Syntax = enumerate(iterable, start)
x = ('apple','banana','cherry')
print(type(enumerate(x)))
print(list(enumerate(x)))
print(list(enumerate(x,10)))
grocery = ['flowers','vegetables','fruits']
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))
print(list(enumerateGrocery))
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
##id() returns unique id for the specified object
x = ('apple''banana','cherry')
print(id(x))
##