n= int(input("enter number of elements : "))
l=[]
for i in range(0,n):
    t=eval(input("enter data : "))
    l.append(t)

c=0
for i in l:
    if isinstance(i,tuple):
        break
    else:
        c+=1
print("elements in a list before tuple : ",c)
