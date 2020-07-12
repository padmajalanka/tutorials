topic = "Today's Topic is Strings"
print(topic.center(55,"*"))
#Strings
"""
String literals in python are surrounded by either single quotation marks,
 or double quotation marks. we can display a string literal with the print() function:
"""
print("Hello good Morning!")
print('Hello Good Morning!')
print("--------------------------")
#  Assign String to a Variable
a = "GoodMorning"
print(a)
print("---------------------------")
#Multiline strings
# we can use double Quotes for multiline strings
s = """ Hi Girls ! Good Morning. Today is very bright day.
Just had a coeffee and want to do little bit of homework."""
print(s)

#we can use single quotes for multiline strings
s= '''Hi Girls ! Good Morning. Today is very bright day.
Just had a coeffee and want to do little bit of homework.'''
print(s)
print("--------------------------------------------------------")

#Strings are Arrays
# Python does not have a character data type, a single
# character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.
v = "Hi,Good Morning!"
print(v[5])
print("------------------")
# SLICING: We can return a range of characters by using the slice syntax.
#
# Specify the start index and the end index,
# separated by a colon, to return a part of the string.
s1 = "Hello where are you?"
print(s1[3:8])                    # This is Indexing
print(s1[2:12])

# negative Indexing
print(s1[-9:-4])                 # negative indexing
print(s1[-5:-2])
print("----------------------------------")

# STRING LENGTH :To get the length of a string, use the len() function.
s1 = "Hi, How are you?"
print(len(s1))                  #To find the length of the String
print("----------------------------------")

# String Methods:
# 1.The strip() method

s1 = "    Hi,let's have a coffee"
print(s1.strip())                       #removes white spaces at begining or end
print("----------------------------------")

#2. Lower()
s1 = "HI, Shall We Go Out"          # returns the string in lower case.
print(s1.lower())
print("----------------------------------")

#3. Upper()
S1 = "hi, what are you doing?"
print(s1.upper())                  # returns the string in uppercase
print("----------------------------------")

#4.Replace()
s1 = "Hi, Have a Good Day!"
print(s1.replace("a","i"))      # replaces the string with another string
print("----------------------------------")

#5. Split()
s1 = "I have  homework to do , don't disturb me"
print(s1.split(" "))            # splits the string into sub strings
print("----------------------------------")

#6. Check String : if a certain phrase or character is present in a string,
# we can use the keywords in or not in.
c = "It's raining ,kids are playing outside"
s = "ds" in c
print(s)
s = "lay" not in c
print(s)
print("----------------------------------")

#7.String Concatenation
var1 = "Hi"
var2 = "Goodmorning"
var3 = var1 + var2
print(var3)
#to add a space between of them is
var3 = var1 + " " + var2
print(var3)
#if we want to put ","
var3 = var1 + "," + var2
print(var3)
print("------------------------------------------------")
#we can't combine strings and numbers'
#by using string format we can combine strings and numbers

#8. Format() method:we can combine strings and numbers by using the format() method!

"""
we can combine strings and numbers by using the format() method!
The format() method takes the passed arguments,
formats them, and places them in the string where the placeholders {} are:"""
#ex
age = 45
name = "My name is Padmaja and i am {}"
print(name.format(age))

"""
The format() method takes unlimited number of arguments, and are placed 
into the respective placeholders:
"""
threepointers= 10
freethrows = 5
totalpoints = 60
score = "the team scored {0} points with {1}freethrows and {2}threepointers "
print(score.format(totalpoints,freethrows,threepointers))
score1 = "the team scored {} points with {}freethrows and {}threepointers"
print(score1.format(totalpoints,freethrows,threepointers))
print("--------------------------------------------------")
#Ex2
quantity = 5
itemname = "sarees"
price = 15.50
myorder = "i want{} pieces of item{} for {} dollars"
print(myorder.format(quantity,itemname,price))
myorder1 = "t want to pay{2} dollars for {0}pieces for item{1} "
print(myorder1.format(quantity,itemname,price))
print('----------------------------------------------------------------------')
#9 Escape character :An escape character is a backslash \ followed by the character you want to insert.
#ex:
#var = "I say "Hello" to you" this will give error
str = "i say\"hello\" to you."
print(str)
#"\"
var = 'it\'s alright'         # if we write it's their's like words in single quoteswe can use\'
print(var)
#"\\"
str1 = "this is python \\examples."
print(str1)
#\n
str2 = "Hello this is Padmaja\ni am learning Python."
print(str2)
#\r
str3 = "webcam is not working\ri want it be to work"     #it will give after \r words or sentences
print(str3)
#"\t
str4 = "today i have a class\t i want webcam to my computer'"
print(str4)
#\b
str5 = "hello\b what is that?"   #it will take out before characteror ,space or ,
print(str5)
#octal value
str6= "\110\125\135\145\154"
print(str6)
#hex value
str7 = "\x65\x55\x6c\x6c\x6f"
print(str7)
print("--------------------------------------------------------")
"""Python has a set of built-in methods that you can use on strings.
Note: All string methods returns new values. 
They do not change the original string.
"""
strs = "My Name is Padmaja, i am learning Python ,Python is easy to understand"
#capitalize()
print(strs.capitalize())
#casefold()  Means all lower cases
print(strs.casefold())
#center()
print(strs.center(95))
#count()
print(strs.count("Python"))
#encode()
print(strs.encode())
#endswith()
print(strs.endswith("python"))
#expandtabs
name =" My\t name\t is\t Pa\tdm\taja"
print(name.expandtabs(2))
#Find()
print(strs.find("Padmaja"))
#Index()
print(strs.index("Padmaja"))
#isalnum() means alphanumeric
print(strs.isalnum())
#isalpha     checks all letters in alphabatic
print(strs.isalpha())
#isdecimal
print(strs.isdecimal())
#isientifier()
print(strs.isidentifier())
#islower()
print(strs.islower())
#isprintable()
print(strs.isprintable())
#isspace
print(strs.isspace())
#Istitle()
print(strs.istitle())
#isupper
print(strs.isupper())
#ljust()
print(strs.ljust(15))
#lstrip()
print(strs.lstrip())
#partition()
print(strs.partition("Python"))
#rfind()
print(strs.rfind("Python"))
#rindex()
print(strs.rindex("Python"))
#rsplit()
print(strs.rsplit(","))
#splitlines()
print(strs.splitlines())
#startswith()
print(strs.startswith("My"))
#swapaces()
print(strs.swapcase())
#title()
print(strs.title())
#zfill
print(strs.zfill(0))
print("bye for now")









