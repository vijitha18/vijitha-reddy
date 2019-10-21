# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:18:19 2019

@author: Student
"""

item={"Biscuit": 10,
"BREAD": 20,
"SUGAR": 84,
"JAM": 40,
"CHEESE": 130,
"BOURNVITA": 240,
"TEA POWDER": 200,
"MILK": 30,
"COFFEE Powder": 40,
"CORNFLAKES": 56,
"RICE": 78,
"DAL": 100}
totalcost=0
print(item)
listofitem=input("enter the item").split(" ")
print(type(listofitem))
for i in listofitem:
    if i in item:
        totalcost=totalcost+item[i]
print(totalcost)
        