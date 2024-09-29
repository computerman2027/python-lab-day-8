def lsearch(l,n):
    for i in range(len(l)):
        if l[i]==n:
            return i
    return -1
def bsearch(l,n):
    low=0
    high=len(l)-1
    while(low<=high):
        mid=low+(high-low)//2
        if(l[mid]==n):
            return mid
        elif(l[mid]>n):
            high=mid-1
        else:
            low=mid+1
    return -1

n=int(input("Enter number of terms : "))
li=[]
pos=-1
for i in range(n):
    temp=int(input("Enter number : "))
    li.append(temp)
n2=int(input("enter item that need to be searched : "))
choice=int(input("MENU\n1. Linear search\n2. Binary search\nEnter your choice : "))
if(choice==1):
    pos=lsearch(li,n2)
    if(pos!=-1):
        print(f"Element found at {pos+1} position")
    else:
        print("Element not found")
elif(choice==2):
    li.sort()
    print("Sorted list =",li)
    pos=bsearch(li,n2)
    if(pos!=-1):
        print(f"Element found at {pos+1} position")
    else:
        print("Element not found")
else:
    print("Invalid input")