def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


num = int(input("enter the number is:"))
# num = 5
print("the factorial of ", num, "is", factorial(num))

# def recursor():
#     recursor()
# recursor()

square = lambda x: x * x
print(square(2))

###lambda function for odd numbers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(filter(lambda x: (x % 2 != 0), my_list))
print(new_list)
### lambda for odd numbers using map
new_list1 = (list(map(lambda x: (x % 2 != 0), my_list)))
print(new_list1)
mylist = [1, 5, 4, 6, 8, 11, 3, 2]

###double
new_list2 = list(map(lambda x: x * 2, mylist))
print(new_list2)


####more examples for recursion
# recursion for fibonacci number
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2))
# n = int(input("enter a number of terms:"))
# print("fibonacci sequence")
for i in range(5):
    print(fibonacci_recursive(i) , end= " ")

#recursion ex for sum
def sumrecur(num):
    if num <= 1:
        return num
    else:
        return num + sumrecur(num-1)
num = 16
if num< 0:

    print("enter a positive number")
else:
        print(" the sum is", sumrecur(num))
#ex multiplication recursion
a = int(input("enter a: "))
b = int(input("enter b:"))

def recursiveproduct(a,b):
    if a ==0 or b ==0:
        return 0
    if b ==1:
        return a
    return a + recursiveproduct(a,b-1)
print("product of a and b = {}".format(recursiveproduct(a,b)))

####examples of lambda functions
#multiplication in lambda
multiply = lambda x : x*2
print(multiply(10))

x = int(input("enter x is:"))
y = int(input("enter y is:"))
add = lambda x,y : x+y
print(add(x, y))

mult = lambda x,y : x*y
print(mult(x ,y))

sub = lambda x ,y :x-y
print(sub(x,y))


# sen = "I am learnming python programming with my friends"
# words = sen.split()
# print(words)
# new_sen = map(lambda word: len(word), words)
# print(new_sen)
