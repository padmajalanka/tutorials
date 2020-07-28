####Lambda FUnctions

"""the anonymous function,also known as lambda functions.
an anonymous function is a function that is defined without a name.
anonymous functions are defined using the lambda keyword.
"""

####Double
double = lambda x: x * 2
print(double(2))

##remainder
remainder = lambda x: x % 2
print(remainder(7))

###product
product = lambda x, y: x * y
print(product(2, 4))

###addition
addition = lambda x, y: x + y
print(addition(5, 6))

###subtraction
subtraction = lambda x, y: x - y
print(subtraction(6, 4))

###divisionm
div = lambda x, y: x / y
print(div(8, 2))


def testfun(num):
    return lambda x: x * num


result = testfun(10)
print(result(9))
result1 = testfun(1000)
print(result1(9))

###create a lambda function using if condition
## Lambda function to check if a given vaue is from 10 to 20
test = lambda x: True if (x > 10 and x < 20) else False

print(test(7))
print(test(12))
print(test(25))

###without using if condition
test1 = lambda x: x > 10 and x < 20
print(test1(12))
print(test1(23))

listofstring = ['hi', 'this', 'is', 'a', 'very', 'simple', 'string', 'for', 'us']
filteredlist = list(filter(lambda x: len(x) == 2, listofstring))
print('filteredlist: ', filteredlist)

###Filter characters from a string in Python using filter()
strObj = 'Hi this is Padmaja,learning python'
filteredchars = ' '.join(filter(lambda x: x not in ["a", "i"], strObj))
print('filtered charactersv:', filteredchars)

###filter with arrays
array1 = [1, 3, 5, 7, 8, 9, 11, 12, 33, 55, 66, 77, 88, 98]
array2 = [3, 5, 11]
filteredarray = list(filter(lambda x: x not in array2, array1))
print('filtered array:', filteredarray)
