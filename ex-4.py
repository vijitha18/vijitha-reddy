# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:05:06 2019

@author: Student
"""

#p2
def billamount(id1,billamount):
    if(id1>100 and id1<1001):
        print("valid customer")
        if(billamount>=500):
            print("10% discount")
        else:
                print("0% disscount")
    else:
        print("invalid customer")
    
     
    
billamount(101,200)


#p1
def dec_bin(num):
    if(num>1):
        dec_bin(num//2)
    print(num%2,end=' ')
        
        
num=int(input("enter the decimal number"))
dec_bin(num)