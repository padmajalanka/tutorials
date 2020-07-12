topic = "today's topic is Booleans"
print(topic.center(55,"*"))

print(10 > 5)
print(10 == 5)
print(10 < 5)
print("-----------------")
a = 50
b = 30
if b >a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print("-----------------")
print(bool("Hi"))
print(bool(15))
x = "hi"
y = 20
print(bool(x))
print(bool(y))
print(bool("abc"))
print(bool(342))
print(bool(["berry","cherry","pear"]))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool())
print(bool([]))
print(bool({}))
print("--------------------------")
def reading():
    return True
if reading():
    print("YES!")
else:
    print("NO!")


def counting():
    return True
if counting():
    print("YES!")
else:
    print("NO!")

def testing(a,b):
    if a*b > 35:
        ret_value = False
    else:
         ret_value = True
    return ret_value


a = float(input ("enter a: "))
b = float(input("enter b: "))

testing(a,b)
print(testing(a,b))
# firstvalue = bool(testing())
# print(bool(firstvalue))

def multiplication():
    a = 10
    b = 5
    return_value = True
    if a*b > 40:
        return_value = True
    else:
        return_value = False
    return return_value
mul = bool(multiplication())
print(bool(multiplication()))



#isinstance()

x = 20
print(isinstance(x,int))
a = 10.5
print(isinstance(a,int))
c = "45"
print(isinstance(c,int))
print(type(c))

















