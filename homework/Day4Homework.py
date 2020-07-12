# string format()
name = "Raji"
txt = "Me and my friend are going to walk today, her name is {}"
print(txt.format(name))

age = "22"
txt = " My elder son name is Viswanth,and he is {}"
print(txt.format(age))

# Unlimited number of arguments and placed into respective places.
quantity = 2
itemno = 245
price = 23.45
myorder = " I want {} pieces of item{} for {} dollars."
print(myorder.format(quantity, itemno, price))
return_price = False
if price < 24:
    print("True")
else:
    print("False")
# using index numbers{0}etc
myorder = "i want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
if itemno == 245:
    print("True")
else:
    print("False")

# Escape character by using\ followed by the character to insert
txt = "we got books \"shipment\" from Amazon."
print(txt)

# single Quotes and "\"
txt = 'it\'s yours.'
print(txt)
# \\
txt = "it'\\s yours."
print(txt)
# using\n
txt = "it's\nyours."
print(txt)
# carrige return\r
txt = "Hello\rworld!"
print(txt)
# \t
txt = "it's\t yours."
print(txt)
# \b
txt = "it's\byours"
print(txt)
# \f
txt = "it's\fyours."
print(txt)
# \000 octal value
txt = "\110\145\154\154\157"
print(txt)
# \xhh hex value
txt = "\x48\x65\xc6\x6c\x6f"
print(txt)

# Boolean values
print(5 > 2)
print(5 == 2)
print(5 < 2)
x = 100
y = 50
if y > x:
    print("y is greater than x")
else:
    print("y is not grater than x")

# Evaluate values and variables: bool() always evaluate any valueand give you True or False

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 16
print(bool(x))
print(bool(y))

# any string and number,list ,tuple,set,dictionary are true except empty ones.
# Some Values True
bool("abc")
bool(345)
bool(["apple", "cherry", "banana"])
bool(("apple", "grapes", "pears"))
bool({123})
# some values are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool())
print(bool([]))
print(bool({}))


# Function can return a Boolean
def sum():
    return True


a = 10
b = 15

if a > b:
    print("False")
else:
    print("True")
    print(sum())
sum()

# yes
def equal():
    a = 14
    b = 15
    if a ==b :
        print("YES!")
    else:
        print("NO!")
    return

equal()

#Built in String methods
txt = "hi, shall we go to movie."
x = txt.capitalize()
print(x)
x = txt.casefold()
print(x)
x = txt.count("shall")
print(x)
x= txt.encode()
print("encoding")
print(x)
txt = "hi going out."
print("endswith")
y= txt.endswith(",")
print(y)

txt = "h\ti\tg\to\ti\tn\tg"
y = txt.expandtabs(3)
print(y)
txt = "hi going out."
y = txt.find("going")
print(y)
txt="hi going out"
x1= txt.center(15,"*")
print(x1)
print(map)
point = {'x':2, 'y':5}
print('{x} ,{y}')
print("(x,y) is ",'{x},{y}'.format_map(point))

# # Isinstance Built in Function
x = 250
print(isinstance(x, int))
print(x)

