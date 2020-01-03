# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 23:56:22 2020

@author: sansin03
"""

#strings
str1 = "sandeep"
str2 = "pratap"
str3 = str1 + " " + str2
print(str3)
a = 10
print(hex(id(a)))
a = 10
a = str(a)
print(hex(id(a)))

##inputgives you a string so must cast if working with numbers
#a = input("Enter a number")
#print(a)
#print(hex(id(a)))
#
#x = float(input("Enter a number for x: "))
#y = float(input("Enter a number for y: "))
#if x == y:
#    print("x and y are equal")
#if y != 0:
#    print("therefore, x / y is", x/y)
#elif x < y:
#    print("x is smaller")
#else:
#    print("y is smaller")
#print("thanks!")

# more complicated with while loop
n = 0
while n < 5:
    print(n)
    n = n+1
    
for n in range(5):
    print(n)

i =10
#default values are start = 0and step = 1and stop as option
for i in range(1, 5):
    print(i)
    
#range(start,stop,step)
for i in range(1, 5, 2):
    print(i)
    
