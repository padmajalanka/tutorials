print("if...else...condition")

##3Ex
a = 5
b = -10
c = 1.5
if a > 0:
    print("a is positive")
else:
    print("a is negative")

if a >= 3:
    print("a:", a)
elif a < 3:
    print("a:", a)

if a >= 3 and a < 10:
    print('a :', a)

if a < b:
    print("a:", a)
elif a > b:
    print("b:", b)

x = True
if not x:
    print("x is False", x)
elif x:
    print(x)

age = 18
if (age >= 8) and (age <= 12):
    print("you are welcome")
else:
    print('sorry!')

var = 'N'
if (var == "Y" or var == 'y'):
    print('yes')
elif (var == 'N' or var == 'n'):
    print('no')
else:
    print('invalid')

a = 10
b = 20
if (a > b):
    pass
else:
    print('b<a')

# Months = { 'Jan': 31,'feb': 28days':'31days','April': '30days',
#            'May': '31days','June':'30days','july':'31days','Aug':'31days',
#            'Sep': '30days','oct': '31days','nov':'30days','Dec': '31days'}


months_list = {
    'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31,
    'June': 30, 'July': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31,
    'Nov': 30, 'Dec': 31
}
# for x in months_list.getKeys() print (x) # if (months_list.get(x) > 30)
[print(x) for x in months_list.keys() if months_list.get(x) > 28]
# print(months_list)
# print(months_list['Jan'])

###HomeWork
# if else
i = 20
if i < 15:
    print("i is smaller than 15")
else:
    print( "i is greater than 15")

#using elif
a = 20
b = 35
c = 45
if a>b:
    print("a is greaterthan b")
elif a < b :
    print("a is lessthan b")

if a < b and a<c:
    print("a is lessthan b and c")
if a <b and a<c: print("a is lessthan b and c")
if a> b or a < c: print("value of a:" , a,"value of b:",b,"value of c:" , c)

## using if elif else
var1 = 50
var2 = 50
if var2>var1:
    print("var2 is greaterthan var1")
elif var2 == var1:
    print("var1 is equal to var2")
else:
    print("var1 is greaterthan var2")

##Nested if
num = 15
if num > 0:

 if num == 0:
    print("zeror")
 else:
     print("positive number")

else:
 print("negative nbumber")

 ##ex 2
#age =int (input("please Enter your age here:"))

if age < 18:
    print("you are Minor")
    print("you are not eligible to wrk")
else:
    if age >= 18 and age<=60:
        print("you are eligible to work")
        print("please fill your details")
    else:
        print("you are too old to work")

##Ex 3
total = 100
country = "US"
if country == "US":
    if total <= 50:
        print("shipping cost is $50")
    elif total <= 100:
        print("shipping cost is $25")
    elif total <=150:
        print("shipping cost is $5")
else:
        print("free")

##EX 4
def operations(operator,x,y):
    if operator == "add":
        print(x+y)
    elif operator == "sub":
        print(x-y)
    elif operator == "mul":
        print(x*y)
    elif operator == "div":
        print(x/y)
x = float(input("enter the value of x:"))
y = float(input("enter the value of y:" ))
operator = input("Enter operator: ")
print(operations(operator,x,y))

##EX5
num1 = int(3.0)
num2 = float(5)
if type(num1) is float:
    print("data type of num1 is float")
else:
    print("datatype of a is int")
#in one statement
print('datatype of a is float')if type(num1) is float else print("datatype of a is int")

##ex6
a1= -6
b1= 5
if type(a1) is int:
    print("datatype of a is int")
    if type(a1)is complex:
        print("datatype of a is complex")
    else:
        print("a1 is int type and it's value is ", a)


if type(a1) is int: print("a1 is int")
print("a1 is complex")if type(a1) is complex else print("a1 is an integer and it's value ia",a)






