# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:21:44 2019

@author: Student
"""

def acceptlogin(u,p):
    if u in users:
        if users[u]==p:
            print("correct")
        else:
            print("incorrect")
    else:
        print("incorrect")



users={}
N=int(input("enter N"))

for i in range(0,N):
    u=input("enter the username")
    p=int(input("enter the password"))
    users[u]=p
checkuser=input("enter the username to check")
checkpassword=input("enter the password to check")
acceptlogin(checkuser,checkpassword)
