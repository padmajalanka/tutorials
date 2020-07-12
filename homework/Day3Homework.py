# Constructor functions
a = int(2)
b =  int(3.5)
c=  int("7")

#print("The type is " + str(a) + str(b) + str(c))
print( a,b,c)
print("int type",a,b,c)

# float()
a = float(2)
b = float (2.8)
c = float("5")
print( a,b,c)
print("float type ", a,b,c)
#
# #string()
a = str("e1")
b = str(2)
c = str(2.5)
print( a,b,c)
print("str type", a,b,c)






#String literals
#String literals in python are surrounded by either single quotation marks, or double quotation marks.
print("hey! go out!")
print('hey! go out!')
#Assigning String Values
a = "hey! go out!"
print(a)

#Multiline String   :You can assign a multiline string to a variable by using three quotes:

x = """ Hey! Today is ToliEkadasi.
     I completed my Pooja and cooking.
     It tooks so long to me.
     Everybody is starving,when i am in pooja.
     i finished it , served lunch for them.
     Now i am doing my homework. It's awesome to learn Python with friends Sudha, kiran.
     learning some good things from both of them. 
"""
print("after double quotes, x value ia " + x)

x1 =  '''  Hey! Today is ToliEkadasi.
     I completed my Pooja and cooking.
     It tooks so long to me.
     Everybody is starving,when i am in pooja.
     i finished it , served lunch for them.
     Now i am doing my homework. It's awesome to learn Python with friends Sudha, kiran.
     learning some good things from both of them.                        '''
print('after single quotes, x1 value is:'  + x1)
# strings are arrays
print( "the 2nd place of string value is " + x[3])

#slicing
print("Get the characters  from the position 9 t0 25 th place of string  is ," + x [9:25])

#Negative Indexing
print("Get the characters from position 15  to position  8 is ,"   +  x[-15:-8])

#string length
print("The length of the string x is" , + len(x))


#String Methods Strip()
print("removing whitespaces from begin or end of the string is ," + x.strip())

#string lower()
a = "Sudha, Me and Kiran finshed yesterday's homework"
print("lower case of string is ," + a.lower() )

#string upper()
print("upper case of the string is, " + a.upper())

# string replace()
print(a, a.replace("M","Y"))
print(a[3:6],a.replace("h","b"))

#Split()
print(a.split(","))
print(a[5:9] , a.split(" "))

#Check String
txt= "Have a good day!"
x = "good" in txt
print(x)
y = "day" not in txt
print(y)


#String Concentation
x= "Good"
y ="Night"
z=x+y
print(z)
print(x + " " + y)























