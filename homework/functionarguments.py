def greet(name, msg):
    """
    Hi Sudha Kiran is explaining Python in a simple way."""

    print("hello", name + ',' + msg)


greet("Sudha", "Good morning")  #


# greet("kiran") gives an error
# greet() with no arguments gives an error
def greet(name, msg="how do you do"):
    print("hello", name + ' , ' + msg)


greet("Kiran")
greet("Sudha", "How do you do?")


# def greet (msg = "Hi!"):
#     print("Hi")            #It gives error
# greet(msg)
def friends(name="sudha", msg="did you finish your work?"):
    print(name + msg)


name = " kiran"
print(friends(name))


def friends():  # function with no arguments
    print("hello , what are you watching")


friends()


def familygod(name):  ####function with one argument
    print(name + " ", "is our god")


familygod("Rama")
familygod("Hanuma")
familygod("saibaba")


def medicine(name, msg):
    print("Hi " + name + ' ,' + msg)


medicine("Advil is ", "medicine for fever")
# ret_message = medicine("Sriram ", "did you took the medcine?")
# print("hello: ", ret_message)


print(" hey ", medicine("Sriram ", "did you took the medcine?"))  # it prints none and name,message
medicine(msg="medicine for fever", name="Advil is")  ## 2  keyword arguments
medicine("Advil is", msg="medicine for fever")  # 1 positional, 1 keyword argument


# medicine(name = "Advil is " , " medicine for fever") having a positional argument after a keyword argument givws error

def task(name, msg="come for dinner"):
    print("Hello " + name + ' ,', msg)


task("Viswanath")
task("viswanath", "come for dinner")
task(name="guys", msg="how is the dinner?")
task("sriram", msg=" can you also sit for dinner")


# task(name = "sriram" ,msg)   ### this will give error message

def call(*names):
    """
    this function call all the names of  person
    :param names:
    :return:
    """
    for name in names:
        print("hello", name)


call("Sriram", "Viswanath", "Sai", " Hari")


###Example pof return straytement
def absolute_value(num):
    """ This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))
print(absolute_value(-4))


def my_num():
    x = 10
    print("value inside function", x)


x = 20
my_num()
print("value outside function", x)


##Python Arbitrary Arguments
def favourite(*fruits):
    for fruit in fruits:
        print("tasty", fruit)


favourite("banana", "apple", "grapes", "watermelon")


###another example
def favor(**fruits):
    for i in fruits:
        print(i, fruits[i])


favor(a="banana", b="apple", c="grapes", d="watermelon")


##another example
def cal(a, b, c):
    print(a, b, c)


dict = {'a': 'cricket', 'b': 'basketball', 'c': 'john'}
cal(**dict)

