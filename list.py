n=int(input("Enter the size of list:\n"))
list1=[]
list2=[]
for i in range(n):
    e=int(input("enter the numbers"))
    list1.append(e)
print("the input list is")
for i in list1:
    print(i)
    if i>=1 and i<=100:
        list2.append(i)
print("the new list is")
for i in list2:
    print(i)        
        
   
    
    
#Q2.2    
L1=['box','pen','chalk','book','cup','bag','pen','box']
output=[]
for i in L1:
    if i not in output:
        output.append(i)
print(output)



#Q2.3
c=['Brazil','Russia','India','China','South Africa']
s=input("enter list of country").split(",")
for i in s:
    if i not in c:
        print("country not found",i)
        
        
#

        
        
        
        
