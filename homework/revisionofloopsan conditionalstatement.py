import datetime
from typing import Dict

import datetime as datetime

a = 2
b = 3.5
c = 1+3j
print("type(a)is:",type(a),a)
print("type(b)is:",type(b),b)
print("type(c) is:",type(c),c)

if type(a)is int:
  print("datatype of a is int")
  if type(a)is float:
        print("datatype of a is float")
  else:
        print("datatype of a is integer:", a)

i = 3.5
while i <= 3.5:
    print(i)
    i += 1
else:
    print("i is  equal to :", i)

i = 1
while i is int:
    if i is complex:
      print("i is complex")
else:
    print("i is not complex")
    i += 1
    print(i)


# if condition for list
total_students_list = ["Sudha", "Kiran", "Padmaja"]
today_student_attendee_list = ["Sudha", "Kiran"]
print('total_students_list: ', total_students_list)
print('today_student_attendee_list: ', today_student_attendee_list)
if  today_student_attendee_list != total_students_list:
    print("the class will not start, bacuse some students are missed the class")
else:
     print("the class will start")


# while loop for list
print(len(total_students_list))

while len(total_students_list)<=3:
    if len(total_students_list)< 3:
        print("the class will not start because of miised students in the class")

    else:
        print("the class will be there")
        print(total_students_list.reverse())
        total_students_list  += "1"
        print(total_students_list.insert(4 , "python"))


# for loop for list

for x in (total_students_list):
    print("total_students_list")

    for x in range(3):
        print(total_students_list)
    else:
        print("finally finished")


fruits = ["apple","banana","grapes","cherry"]
for x in fruits:
    print("fruits:", fruits.copy())



list = ["apple","banana","grapes","cherry"]
i = 0
while i < len(list):
    print(len(list))
    element = list[i]
    i += 1
    if element != "cherry":
        print("fruit", element)
        continue



#####STRINGS
name = "Padmaja"
print("Padmaja")
print(len(name))
# strings for loop
for word in name:
    print("letters are:",name)
    print("letters are :" ,name.upper())
    print("letters are :" , name.lower())
    print("letters are:", name.count("a"))
    print(name.replace("j", "h"))
    print(name.split("Padma"))
#print("-----\n")

for word in range(len(name)):
    print("letters at {0}is = {1}". format(word , name[word]))
### strings while loop

name = "padmaja"
if name == "sudha":
    print("name is not correct")
else:
    print("correct name:", name)
##### dictionaries
###if condition
mykey = "two"
my_dict = { "one": "Vegitables", "two": "fruits","three": "juice","four":"frozen"}
if mykey in my_dict:
    print("the given key exists")
else:
    print("the given key does not exist")

myvalue = "snacks"
if myvalue in my_dict:
    print("the value exists")
else:
    print("the value does not exists")
print( my_dict.get("two","fruits"))
print(my_dict["three"])

my_dict = { "one": "Vegitables", "two": "fruits","three": "juice","four":"frozen"};
for key, value in my_dict.items():
    print(key)
    print(value)
    print(key, value)
    print((my_dict).get("three"))


####Tuple
fruits = ('apple','orange','pear','peach')
for fruit in fruits:
    print(fruit)
    if len(fruits) > 5:
        print("length of the fruits is not graterthan 5")
    else:
        print("the length of the fruits is:",len(fruits))
while len(fruits)>5:
    print("length is not 5")

else:
    print("the length of fruits isnot  5")

####sets
set_evennum = {2,4,6,8,10,12}
set_oddnum = {1,3,5,7,9,11,13,15}
newset = set_evennum |set_oddnum
print(newset)
for evennum in newset:
    print(evennum)

    if len(set_oddnum)< len(set_evennum):
        print("the length of odd numbers is smallerthan length of even numbers:",len(set_oddnum))
    elif len(set_oddnum) == len(set_evennum):
        print("length of odd numbers is equal to length of even numbers","len(set_evennum", len(set_oddnum))
    else:
        print("length of odd numbers is greater than length of even numbers")















