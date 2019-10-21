# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:46:34 2019

@author: Student
"""

graph={"PC1":["PC2","PC4"],"PC2":["PC1","PC3","PC5"],"PC3":["PC5","PC2"],"PC4":["PC1","PC5"],"PC5":["PC4","PC2","PC3"]}
print(graph)
print("First")
first=graph["PC1"]
print(first)
second=[]
for i in first:
    test=graph[i]
    for j in test:
        if(j not in second and j!="PC1" and j not in first):
            second.append(j)
            
print("second neighbours")
print(second)