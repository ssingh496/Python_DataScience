# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 02:08:06 2019

@author: sansin03
"""
thisDic = {"key1":"sandeep", "key2":"pratap", "key3":"singh"}
print(thisDic)
print(thisDic.keys)
print(thisDic.items)

print("\nthis Dics")
for i in thisDic:
    print(i)

print("\nthis Dics[i]")    

for i in thisDic:
    print(thisDic[i])

print("\nthis Dict.value()")        
for x in thisDic.values():
  print(x)

print("\nthis Dict.itmes()")
    
for x , y  in thisDic.items():
  print(x)
  print(y)
  
supported  = ["san", "key2", "sin"]

unsupported_layers = [l for l in thisDic.keys()]
print(unsupported_layers)
