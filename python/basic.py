# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

@author: xuguoqi
"""

greeting="Hello"

print(greeting)

type(greeting)

greeting2="hello"


mystring='hello world!'
print(mystring)

type(mystring)
len(mystring)

name='alken'
greeting = 'hello, ' + name
print(greeting)

a=10
print(a)
b=-100
print(b)
c=0
print(c)

c='sfd'
print(c)

#float exercise
x = 1
y = 2
z = 3


# built-in funcitions
dir(__builtins__)

int(10.5)

#list 
address= ['tokyou street',18,'tokyo']

print(address[0],address[1])

days=['mon','tue','wed','thu','fri','sat','sun']

days[0:3]
days[:4]
days[1:3]
days[0:-1]

address.append("japan")
address.remove('japan')
address.pop(1)

address.append(20)

#list 
address2= ['tokyou street',18,20.1]

# dictionaries
pins = {"Mike":1234, "Joe":1111, "Jack":2222}

pins['Mike']
type(pins["Mike"])
pins.keys()
pins.values()

person80 = {"name":"Jayden", "Surname":"alken", "age":30}
person80.pop("name")

person80["name"]="alken xu"

person80["age"]=31

# mapping two lists to a dictionary
keys=['a','b','c']

values=[1,2,3]

myDist= dict(zip(keys,values))

#user input
pin = int (input("enter your pin: "))
print(pin**2)

# multiple conditions
user_input = float(input("enter number: "))

if user_input > 100:
    print("greater")
elif user_input == 100:
    print("equal")
else:
    print("smaller")
