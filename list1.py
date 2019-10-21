# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 03:47:55 2019

@author: Student
"""

L1=[]
L2=[]
n=int(input("enter the value of n"))
for i in range(0,n):
    x=int(input("enter the list values"))
    L1.append(x)
m=int(input("enter size of second list"))
for i in range(0,n):
    x=int(input("enter the list values"))
    L2.append(x)
for i in L1:
    if L1 not in L2:
        print("removed value",i)
        print(L1.index(i))
        print("position",L1.index(i))