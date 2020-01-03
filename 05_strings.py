# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 00:22:52 2020

@author: sansin03
"""

#there is no issues in conparing 
a =10
b = "sandeep"

if a!=b:
    print("there is no match")

name = "sandeep"
print(len(name))
b = int(len(name))
for i in range(len(name)):
    print(name[i])
    if name[i] =='s':
        print("there is a match")

sampleStr = "Hello!!"
 
print("**** Iterate over string using for loop****")
 
for elem in sampleStr:
    print(elem)
#
#STRINGS
#can slicestrings using [start:stop:step]
#if give two numbers, [start:stop], step=1by default
#you can also omit numbers and leave just colons
#6.0001 LECTURE 3 6
#s = "abcdefgh"s[3:6] evaluates to "def", same ass[3:6:1]s[3:6:2] evaluates to "df"
#s[::] evaluates to "abcdefgh", same as s[0:len(s):1]s[::-1] evaluates to "hgfedbca", same as s[-1:-(len(s)+1):-1]
#s[4:1:-2] evaluates to "ec"

  #0ve sign means it will start backward.
s = "abcdefgh"
print(s[::-1])
print(s[4:1:-2])

#same as c strings are mutable
s = "hello"
#s[0] = 'y' #gives an error
s = 'y'+s[1:len(s)]