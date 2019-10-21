# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 05:02:52 2019

@author: Student
"""

L= ['bus', 'train', 'flight', 'boat', 'ship'] 
output=[]
for i in L:
    if i not in output:
        output.append(i)
print(output)