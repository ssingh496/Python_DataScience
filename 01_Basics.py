# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 23:14:27 2020

@author: sansin03
"""

a= 10
print(a)
print(hex(id(a)))

a= 20
print(a)
print(hex(id(a)))
b = 10
print(hex(id(b)))

#in python you are assigning new mmeory address at each time. It's the same memory address. 
a=10.5
print(a)
print(hex(id(a)))
a= "sandeep"
print(a)
print(hex(id(a)))
b= "sandeep"
print(b)
print(hex(id(b)))
#it the python which do the mapping with the handler for you. and same value gets the same handler. 

pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment
area = pi*(radius**2)
print(area)

# change values of radius <- another comment
# use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
area = pi*(radius**2)
print(area)

#multiple comment/uncomment happens with cntrl+1 

