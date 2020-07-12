print(" HI FRIENDS, TODAY'S HOMEWORK")
txt = "Arithematic operators"
x = txt.center(50,"*")
print(x)

#"+" operatoe
x= 10
y= 15
print(s5um)
print('x+y=', x+y)

print("sub")
print('x-y=', x-y)

print("mult")
print('x*y= ',x*y)

print('div')
print('x/y= ',x/y)

print("mod")
print('x%y= ',x%y)

print('expo')
print('x**y = ',x**y)

print("floor div")
print('x//y= ',x//y)

#Python assignment operators
# equal operatoe " = "
x= 5
print(x)
print("+=")
x=5
x += 3
print(x)

print("-=")
x = 5
x -= 4
print(x)

print("*=")
x= 5
x *= 3
print(x)

print("/=")
x = 5
x /= 5
print(x)

print("%=")
x= 5
x %= 3
print(x)

print("//=")
x = 5
x //= 3
print(x)

print("**=")
x = 5
x **= 3
print(x)

print("&=")
x = 5
x  &= 3
print(x)

print("|=")
x = 5
x |= 3
print(x)

print("^=")
x = 5
x ^= 3
print(x)

print(">>=")
x = 5
x >>= 3
print(x)

print("<<=")
x = 5
x <<= 3
print(x)

# Python Comparision operators
print("==")
x = 5
y = 3
print("x ==y is " ,x == y)
print('x != y is' , x!=y)
print('x > y is' , x>y)
print('x < y is ' , x<y)
print('x >= y is ' , x>=y)
print('x <= y is ', x<=y)

# Python Logical operators
print('and operator')
x = "banana"
y = "orange"
print('x and y is', x and y)
print('x or y is', x or y)
print('not x is ',not x)

#special operators
print("is operator")
x = 5
y = 4
print('x is y true is ', x is y)
print('is not operator')
print('xis not y is ', x is not y)

# Membership operators
print('x in y')
x = ['apple','Banana']
print('apple' in x)
print('x not in y')
print('orange'not in x)

#Python Bitwise operators
#--------------------------
print("& operator")
x= 9
y= 65
print("Bitwise and operator on 9 and 65 is", x&y)
print("bitwise or operatoro")
print("bitwise or operator on 9 and 65  is" , x|y )
print("bitwise or ^ operator")

print("bitwise Exclusive operator or ison 9 ans 65 is", x^y)
print("bitwise operator not")
print("bitwise not operator on 9 and 65is", ~x )
print('bitwise left shift operator << ')
print("bitwise left shift operator on) 9 and 65 is", x<<1)
print("bitwise right shift operatoe >>")
print("bitwise right shift operatoe on 9 and 65 is ", y>>1)

     #python arithematic operators on strings

a = "Tutorial"
b=  "Python"
print(a + b)
print(a + " " + b)
print(a * 3)
print((a + " ")* 3)
print(a + str(3))

      #Python arithematic operators
def arithematic_operations(x,y,operator):
    if operator == 'sum':
        return x + y
        print(x + y)
    if operator == 'sub':
        return x- y
        print(x - y)
    if operator == 'mult':
        return x*y
        print(x*y)
    if operator == 'div':
        return x/y
        print(x/y)
    if operator == 'mod':
        print(x%y)
    if operator == 'expo':
        print(x**y)
    if operator == 'floor div':
        print(x//y)

        # Pythom Comparision operators
    if operator == 'equal':
        print(x ==y)
    if operator ==  'is not equal':
        print(x != y)
    if operator == 'greaterthan':
        print(x > y)
    if operator == 'less than':
        print(x < y)
    if operator == 'greater than or equal to':
        print(x >= y)
    if operator == 'less than or equal to':
        print(x <= y)


# Python Logical operators
    if operator == 'and':
        print(x > 3 and y > 5)
    if operator == 'or':
        print(x < 5 or y < 5)
    if operator == 'not':
        print(not(x < 3 and y<4))
x = float(input("Enter x: "))
y = float(input("Enter y: "))
operator = input("Enter operator: ")
print(arithematic_operations(x,y,operator))

# without giving  operators:
#by using methods
val1 = 78
val2= 5
sum = float(val1) + float(val2)
print("the sum of two given numbers is ",sum)

# by using format()
num1 = float(input('enater the first number: '))
num2 = float(input('enter the second number: '))
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
# same way we can do sub,mult and other operations.





