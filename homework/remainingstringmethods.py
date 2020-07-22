### by using dictionary for format_map()

type = input("enter type:")
brand = input("enter brand:")
selection = "i like wear {} with the {} brand "
print(selection.format(type,brand))
dict= {"type": "Shoes" , "brand": "nike" }
print(selection.format(dict["type"],dict["brand"]))
print('{type} {brand}'.format_map(dict))

 #join()	Joins the elements of an iterable to the end of the string
sentence = "today i want to finish my homework early that is "
print(sentence.join('python'))
dict1= {"course": "python" , "type": "homework" }
print(sentence.join(dict.keys()))
print(sentence.join("python").split(" "))
print(sentence.join('python').strip())
print(sentence.join('python').isalpha())
sen = "ilike,tocooknow"
print(sen.isalpha())

print(sen.join('cricket').split(","))
print(sen.join('hi').casefold())

# ljust()	Returns a left justified version of the string
print(sen.rjust(25))
print(sen.rjust(30, '$'))
# lower()	Converts a string into lower case
sen1 = "             I LIKE SWEETS                "
print(sen1.lower())
print(len(sen1))
# lstrip()	Returns a left trim version of the string
print(sen1.strip(' '))

# maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
sen2 = " I LIKE SWEETS "
print(sen2.partition("SWEETS")) ##search for sweets and returns a tuple three elements
print(sen2.partition("FRUITS")) ####f the specified value is not found, the partition() method
# returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:

##replace()	Returns a string where a specified value is replaced with a specified value
print(sen2.replace("SWEETS","fruits"))
sen3 = "i like sweets,sweets are in taste sweet"
print(sen3.replace("sweets","fruits",2))
