# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:35:56 2019

@author: Student
"""

customerdetails= {1001: "John", 1004: "Jill", 1005: "Joe", 1003: "Jack"}
print(customerdetails)

print(len(customerdetails))

for x in sorted(customerdetails):
    print(x,customerdetails[x]) 
    
print(customerdetails.pop(1005))
print(customerdetails)

customerdetails= {1001: "John", 1004: "Jill", 1005: "Joe", 1003: "Jack"}
customerdetails[1003]="Mary"
print(customerdetails)

if 1002 in customerdetails:
    print("yes")
else:
    print("no")    