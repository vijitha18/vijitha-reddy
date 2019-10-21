# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:30:16 2019

@author: Student
"""

Mobile={"brand": "samsung", "model": "S10", "Screen size":6.1}
print(Mobile)

print(Mobile["model"])
print(Mobile.get("model")) 

Mobile ["model"] ="S11"
print(Mobile)

for i in Mobile:
 print(i)

for i in Mobile:
    print(Mobile[i])

for i in Mobile.values():
 print(i)

for x,y in Mobile.items():
 print(x,y)

if "model" in Mobile:
 print("yes")

print(len(Mobile))

Mobile["colour"]="white"
print(Mobile)

print(Mobile.pop("model"))
print(Mobile)

print(Mobile.popitem())
print(Mobile)

del Mobile['brand']
print(Mobile)

myfamily ={
 "child1" : {
 "name" : "Iniyan",
 "year" : 2004
 },
 "child2" : {
 "name" : "Raja",
 "year" : 2007
 },
 "child3" : {
 "name" : "babu",
 "year" : 2011
 }
}
print(myfamily)
print(myfamily["child1"])
print(myfamily["child1"]["name"])

Customerdetails = {1001: "John", 1004: "Jill", 1005: "Joe", 1003: "Jack"}
for x in sorted(Customerdetails):
    print(x,Customerdetails[x])