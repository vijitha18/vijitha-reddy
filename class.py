# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 03:48:01 2019

@author: Exam
"""

class person:
    def __init__(self,name,number,mobilenumber,address):
        self.name = name
        self.number = number
        self.mobilenumber = mobilenumber
        self.address = address
class student(person):
    def setdata(self,branch,studenttype,cgpa):
        self.branch = branch
        self.studenttype = studenttype
        self.cgpa = cgpa
    def getdata(self):
        return(self.name,self.number,self.mobilenumber,self.address,self.branch,self.studenttype,self.cgpa)

class professor(person):
    def setdata(self,typeofemployment,subjecttaught,salary):
        self.typeofemployment = typeofemployment
        self.subjecttaught = subjecttaught
        self.salary = salary
    def getdata(self):
        return(self.name,self.number,self.mobilenumber,self.address,self.subjecttaught,self.typeofemployment,self.salary)

S1=student("raja",201,"957304277","kormangala,bengaluru")
S1.setdata("cse","dayscholar",7)
print(S1.getdata())
P1=professor("elango",1001,"7658942336","Anna nagar,Chennai")
P1.setdata("Parttime","python",50000)
print(P1.getdata())         