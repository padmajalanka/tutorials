topic = "clearinmg doubts in class{}"
print(topic.format(topic))
course = "python"
week = 5
participant = 3
topic = "all {} participants meet{} times a week and practice {} everyday"
print(topic.format(participant,week,course))

topic = "all {0} participants meet {1} times a week and practice {2} everyday"
print(topic.format(week,participant,course) +  "Everyday")
print(topic.index('practice'))
print("substring practice is:" , topic.index("practice"))
###substring with arguments
#print("substring practice is:" , topic.index("program"))

####Today's Homework
#####Arithematic operations in function
# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:
# Operator	                             Name
# +	Addition	                         x + y
# -	Subtraction                          x - y
# *	Multiplication	                     x * y
# /	Division	                         x / y
# %	Modulus	                             x % y
# **	Exponentiation	                 x ** y
# //	Floor division	                 x // y

x = int(input("enter x is:"))
y = int(input("enter y is:"))
operator =input("enter a operator is:")
def multi_arithematicoperations(x,y, operator):
    if operator == 'sum':
        return x + y
        print(x+y)
    if operator == 'sub':
        return x - y
        print(x - y)
    if operator == 'mul':
        return x*y
        print(x*y)
    if operator == 'div':
        return x/y
        print(x/y)
    if operator == 'mod':
        return x%y
        print(x%y)
    if operator == 'expo':
        return x**y
        print(x**y)
    if operator == 'floor div':
        return x//y
        print(x//y)

#########Python Comparison Operators
# ==	Equal	                         x == y
# !=	Not equal	                     x != y
# >	    Greater than	                 x > y
# <	    Less than	                     x < y
# >=	Greater than or equal to	     x >= y
# <=	Less than or equal to	         x <= y
    if operator == "equalto":
        return x == y
        print(x == y)
    if operator == "notequalto":
        print(x != y)
        return x != y
    if operator == "greaterthan":
        return x > y
        print(x > y)
    if operator == "lessthan":
        return x < y
        print(x < y)
    if operator == "greaterthan or equalto":
        return x >= y
        print(x >= y)
    if operator == "lessthan or equalto":
        return x <= y
        print(x <= y)
print(multi_arithematicoperations(x, y, operator))
####PYTHON LOGICAL OPERATORS :
# Operator	Description
# and 	Returns True if both statements are true	                x < 5 and  x < 10
# or	Returns True if one of the statements is true	            x < 5 or x < 4
# not	Reverse the result, returns False if the result is true  	not(x < 5 and x < 10)

def logical_operator(x,operator):

    if operator == 'and':
        return x < 5 and x <10
        print(x <5 and x<10)
    if operator == 'or':
        return x<5 or x<7
        print(x<5 or x<7)
    if operator == 'not':
        return( not(x<5 and x<8))

x = int(input("enater x is:"))
operator = input("enter operator is: ")
print(logical_operator(x,operator))



