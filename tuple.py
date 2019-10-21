# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:18:15 2019

@author: Student
"""

fruit = ("apple", "banana" , "cherry")
print(fruit)
print(len(fruit))
print(fruit[1])
print(fruit[-1])
print(fruit[1:2])

x = ("pineapple", "banana", "cherry")
x[1] = "orange"

y = list(fruit)
y[1] = " orange "
fruit= tuple(y)
print(fruit)

for x in fruit:
 print(x)

if "pineapple" in fruit:
 print("Yes, 'apple' is in the fruits tuple")

del fruit

