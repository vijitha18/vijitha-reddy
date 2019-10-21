# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 04:01:25 2019

@author: Student
"""

L1=[1,2,3,4,5,4]
pos=0
n=int(input("enter the number"))
count=0
for i in L1:
    if i==n:
        print(n,"present at",pos)
        count=count+1
    pos=pos+1
print(count)
print(L1.count(n))