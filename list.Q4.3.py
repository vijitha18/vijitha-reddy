# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:08:22 2019

@author: Student
"""

names=input("enter student names").split(' ')
for i in range(0,len(names),-1):
    for j in range(0,len(names),-i-1):
        if names[j]>names[j+1]:
            temp=names[j]
            names[j]=names[j+1]
            names[j+1]=temp
    print(names)
print(names)