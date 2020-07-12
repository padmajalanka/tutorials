o = "Python Operators"
print(o.center(55,"*"))
print("Arithematic Operators")
var1 = 6
var2 = 3
print(var1+var2)
print(var1-var2)
print(var1*var2)
print(var1/var2)
print(var1%var2)
print(var1**var2)
print(var1//var2)

def testingoperators(a,b, operator):
    """

    :type a: object
    """
    if operator == 'sum':
        return a + b
        print(a + b)
    if operator == 'sub':
        return a-b
        print(a-b)
    if operator == "mult":
        return a*b
        print(a*b)
    if operator == "div":
        return a/b
        print(a/b)
    if operator == "mod":
        return a%b
        print(a%b)
    if operator == "expo":
        return a**b
        print(a**b)
    if operator == "floor div":
        return a//b
        print(a//b)
 ##COMPARISION OPERATORS
    if operator == "equalto":
        return a == b
        print(a==b)
    if operator == "notequalto":
        print(a!= b)
        return a != b
    if operator == "greaterthan":
        return a > b
        print(a > b)
    if operator == "lessthan":
        return a < b
        print(a < b)
    if operator == "greaterthan or equalto":
        return a >= b
        print(a >= b)
    if operator == "lessthan or equalto":
        return a <= b
        print(a <= b)

##Logical operators are used to combine conditional statements:
    if operator == "and":
        return a>3 and b>5
        print(a>3 and b>5)
    if operator == "or":
        return a > 3 or b>5
        print(a>3 or b>5)
    if operator == "not":
        return not a>3 and b>5
        print(not(a>3 and b>5))

a = float(input("Enter a: "))
b = float(input("Enter b: "))
operator = input("Enter operator: ")
print(testingoperators(a,b, operator))

# IDENTITY Operators
"""1. Is Operator
Is operator helps users to know if two objects are the same or not? If two objects refer to the same memory location, then Is operator returns “True”. 
, if two objects refer to separate memory locations, the “Is” operator will return “False”."""
#EX 1
m = 30
n = 30
if (m is n):
       print("m and n have same identity")
else:
    print("m and n have same idetity")
#Ex2
m = 30
n = "30"
if (m is n):
    print("m and n have same identity")
else:
    print("m and n do not have same identity")
#Ex3
m = 30
n = 30
if(id(m) is id(n)):
    print("m and n have same identity")
else:
    print("m and n do not have same identity")
    print(id(m))
    print(id(n))
#ex 4
m = 30
n = "30"
if(id(m) is id(n)):
    print("m and n have same identity")
else:
    print("m and n do not have same identity")
    print(id(m))
    print(id(n))
#Ex5
x = 50
if(type(x) is int):
    print("True:if executed")
else:
    print("False:else executed")
#ex6
x = "40"
if(type(x)is str):
    print("True:if executed")
else:
    print("False:else executed")
#ex7
x1= 5
y1 =5
print(x1 is not y1)
x2 =[1,2,3]
y2 = [1,2,3]
print(x2 is y2)
x3="hello"
y3 ="hello"
print(x3 is y3)
#isnot
o = 50
p = 50
if(o is not p):
    print("o and p have same identity")
else:
    print("o and p do not have same identity")
#ex2
q = 50
r = "50"
if(q is not r):
    print("q and r have same identity")
else:
    print("q and r do not have same idetity")
#ex3
s = 50
if(type(s) is not int):
    print("True: if executed")
else:
    print("False: else executed")

#Membership Operators:
# "in " , "not in" are the membership operators.
#Ex In
x = "Hello world"
y = {1:'a',2:'b'}
print("H" in x)
print("hello" in x)
print("hello" not in x)
print(1 in y)
print('a'in y)
#Ex2
x = ["apple" ,"banana"]
print("banana"in x)
print("pineapple" not in x)
print("pine apple" in x)
# Python Bitwise Operators
#ex
a = 9
b = 65
print("Bitwise And operator on 9 and 65 is",a&b)
print("Bitwise OR operator on 9 and 65 is",a|b)
print("Bitwise EXCLUSIVE OR operator on 9 and 65 is",a^b)
print("Bitwise NOT operator on 9  is",~a)
print("BitwiLEFT SHIFT operator on 9 is ",a<<1)
print("Bitwise RIGHT SHIFT operator on 9 is", b>>1)

# PYTHON ASSIGNMENT OPERATORS
#"="
b = 100
print("the initial value of variabl b is " +str(b))
b = 12.27*94.53
print("the value of variable b is" + str(b))
# " += "
b = 100
b += 12.9
print("the value of variable is" +str(b))
# "-="
b = 100
b -= 12.9
print("the value of the variable is " +str(b))
# " *= "
b = 100
b *= 7.57
print("the value of the variable is " +str(b))
# "/= "
b = 100
b /= 1.22
print("the value of the variable is" +str(b))
# "%="
b = 100
b %= 5
print("the value of the variable is " +str(b))
# "//="
b = 25
b //= 7
print("the value of the variable is " +str(b))
# **=
b = 3
b **=4
print("the value of the variable is " +str(b))
#Ex2
p = 10
q =12.5
r = 14.2
sum = p + q
print("sum of"+str(p)+ 'and'+str(q)+ 'is '+str(sum))
sum += r
print(sum)
sum -= r
print(sum)
sum *= r
print(sum)
sum /= r
print(sum)
sum %= r
print(sum)
sum //= r
print(sum)
sum **= r
print(sum)















