i = 1
while i <6:
    print(i)
    if i == 3:
        break
    i += 1


# continue
i = 1
while i < 6:
    i += 1
    print(i)
    if i == 3:
        continue
    print(i)

i = 1
while i < 4:
    print(i)
    break

i = 1
while i < 4:
  if  i ==1:
    print(i)
    break

i = 1
while i <4:
    i += 1
    i += 3
    if i == 4:
        print(i)
        continue

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is lesser than 6 ")

i =0
while i < 10:
    if i%2 == 0:
        print(i)
    i +=1

num = 1
while (num <=100 ):
    if (num % 2) == 0:
        print(num , "is even")

    else:
        print(num , " is odd", )
    num += 1
#EVEN AND ODD NUMBERS
var = 1
while (var <= 100):
    """if var %5 ==0:
        print(var)
    var += 1
"""
    if(var%2)==0:
       # print("{0}is Even".format(var))
         print(var,"is even")
    else:
       # print("{0} is odd".format(var))
         print(var, "is odd")
    var += 1


# PRIME NUMBERS

# Program to check if a number is prime or not

# To take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")

num = 11
if num > 1:
      for i in range(2, num//2):
        if (num % i) == 0:
          print(num, "is not a prime number")
          break
        else:
         print(num, "is a prime number")
else:
          print(num, "is not a prime number")



















