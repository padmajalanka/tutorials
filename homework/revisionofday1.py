# print function
print("this is revision of last weeks homework")

# indentation
if 2 > 6:
    print("2 is greater than 6")

# Comments
# In Python we use "#" sign for comments for single line.
# for multi lines we can use """ """ or ''' '''
""" 
it's so hot outside.
it will  be rain today.
today's temperature high is 90
"""
''' 
it's so hot outside.
it will  be rain today.
today's temperature high is 90
'''
##Variables
# Variables are containers that storing data.
x = 4
y = "Hot"
print(x)
print(y)

# variables can be declared by " " or ' '
x = "Hot"
x = 'Hot'

# Ex
myvar = "In this Summer"
my_var = "There are no IPL Matches"
_my_var = "So may people are waiting to watch IPL matches."
myVar = "Because of Carona "
MYVAR = "They are not playing"
myvar1 = " No Fun in this year"
print(myvar, my_var, _my_var, myVar, MYVAR, myvar1)

# different values to different Variables
x, y, z = "onedaymatches", "T20 matches", "test matches"
print(x)
print(y)
print(z)
print(x, y, z)
print(x, " ", y, " ", z)

# same value to different variables
x = y = z = "T20 matches"
print(x)
print(y)
print(z)
print(x, y, z)

# combine text and a variable
x = "it's raining outside"
print("Padmaja said " + x)
# + character to add one variable to another variable
x = "No classes in this week"
y = "because Sudha is busy with her family "
z = x + y
print(z)
print("i am free  ", x + " ", y)

# + character for mathematical opereator
x = 10
y = 15
print(x + y)
# we can't combine string and a number'

# global variable
x = "Raining"
y = 'July 6th'
z = '3 PM'


def weather():
    print(f"the wather is: {x} on {y} at {z}")


weather()


# global keyword
def games():
    global game_name
    game_name = "cicket"


games()
print("i like games , one of the game name is " + game_name)

# To change the value of global variable inside a function, refer to the variable inside a function
sport = "Kabadi"


def mygame():
    global sport
    sport = "Longjump"


mygame()
print("my favorite game is " + sport)


def sum():
    global x
    x = 5
    y = 6
    return x + y
s= sum()
print("Sum of x and y is "+ str(s))

def sub():
    y = 2
    return  x - y
h = sub()
print(" sub of x and y is "  + str(h))

