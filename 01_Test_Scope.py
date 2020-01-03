# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 02:08:31 2019
this is the example of the scope in python

@author: sansin03
"""
a= 30

def name():
    a= 10
    def subname():
        a=20
        print(a)
    subname()
    print(a)

name()
print (a) #at this stage out will be 30 for global, 20 for local and 10 for local 

print("the scope chnages to nonlocal")
      
def scope():
    a= 10
    def subscope():
        nonlocal a
        a =20
        print(a)
    subscope()
    print(a)      

scope()
print(a)
print("the scope chnages to global")
def globalIn():
    a= 10
    def subglobal():
        global a
        a= 20
        print(a)
    subglobal()
    print(a)      

globalIn()
print(a)

def message(mssg):
    print(mssg)
    #msglcl = "this is message from calling funcation"
    def submsg(mssg):
        print(mssg)
        print(mssg)
        mssg = "this is sub message"
    return submsg

funobj = message ("this is caller function")

funobj("this is funobj")
