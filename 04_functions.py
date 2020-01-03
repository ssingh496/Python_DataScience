# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 00:51:44 2020

@author: sansin03
"""

def findEven(i):
    if(i%2==0):
        print("number is even")
    else:
        print("number is prime")
#Python returns the value None, if no returngiven        

findEven(20)

#inside a function, can access a variable defined outside
#inside a function, cannot modify a variable defined outside --can using global variables, but frowned upon
#when one modify the variable it changes the scope of it.

"""

""" 

i =30
j=50
def scope(i):
    i = i+10;
    print(i)
#UnboundLocalError: local variable 'j' referenced before assignment    
#    j = j+1
#    print(j)
    z=i
    
    return z

scope(i)
print(i)
print(j)

def func_a():
    print ('inside func_a')
def func_b(y):
    print ('inside func_b')
    return y
def func_c(z):
    print ('inside func_c')
    return z()
print (func_a())
print (5 + func_b(2))
print (func_c(func_a))