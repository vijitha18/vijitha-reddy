n=int(input("Enter the size of list"))
age=[]
for i in range(0,n):
    e=int(input("enter the ages"))
    age.append(e)
print("input ages")   
for i in age:
    print(i)
for i in range(len(age)):
    if age[i]>40 and age[i]<50:
        age[i]=['middle age']
print("the modified ages are\n")
for i in age:
    print(i)         