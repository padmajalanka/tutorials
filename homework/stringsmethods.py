print("TODAY's TOPIC is STRING METHODS")
a  = str(5)
b = str(6.7)
c = str("Hi")
print( "string type is:" , a,b,c )
###string in double quotes
a = """In summer, kids go out and play games  like Basketball, Cricket and do cycling with their friends. 
    but in this summer because of this covid-19 kids missing to play outside and meet their friends.
    Me and my friends learning Python. Python easy to learn.we are writing little code also. if i get
    any doubts, my friends Kiran and Sudha are helping to clarify my doubts. it"s little fun too to spend 
    with my friends some time.it"s remebering me my school and college days."""
print(a)
####String in single quotes
b = '''In summer, kids go out and play games  like Basketball, Cricket and do cycling with their friends. 
    but in this summer because of this covid-19 kids missing to play outside and meet their friends.
    Me and my friends learning Python. Python easy to learn.we are writing little code also. if i get
    any doubts, my friends Kiran and Sudha are helping to clarify my doubts. it"s little fun too to spend 
    with my friends some time.it"s remebering me my school and college days.'''
print(b)

####String Arrays,Slicing,Indexing,Negative Indexing,String length
print(a[125]) # string location
print("above a[125] is called indexingthat means string location at 125 th place")

print(b[10:25])    ##prints string from location 10 to 25 called Slicing
print("the above b[10:25] is called string slicing.it means the string from 10th to 25th loaction")

print(b[-20:-10])       #### Negative indexing
print("the above [-20:-10] means  string backwards from the end")

###to find the string length
c = len(b)
print("the length of the string b is", c)

###lower() prints the string into lowercase
print(b.lower())
print("lower case of b is ")

 ####upper() prints the string in uppercase.
print(a.upper())
print("uppercase of a is ")

####strip () strip removes any white spaces from begining to end
print(a.strip())

###Replace() this means relaces the characters
print(b.replace("i","u"))

###replacing with arrays
print(b[145:255])
print(b[145:255].replace("j","k"))

####split()
print(b.split(" "))
###split with array
print(b[123:143].split(" "))

###checking for certain string in the text
print("checking for the string")
c = "kids" in b
print(c)
c = "ing" in b
print(c)

###string concatenation
print("string Concatenation")
a1 = "GOOD"
b1 = "NIGHT"
print(a1+b1)
print(a1 + " "+b1)

###format(
cars = 2
color= "Red"
model = "Toyota"
mystore  = "i have {} of {} color {} cars"
print(mystore.format(cars,color,model))
mystore  = "i have {1} of {0} color {1} cars"
print(mystore.format(color,model,cars))
mystore1 = " i have 6 red toyota cars and 8 Honda vans in my store"
print(mystore1.index('toyota'))
print("substring toyota is:",mystore1.index('toyota'))

#### Escape() An escape character is a backslash \ followed by the character you want to insert.
sen = "they are called very\"tasty\" cookies."
print(sen)

















