d={}
try:
    n=int(input("Enter no of keys in dictionary : "))
    for i in range(n):
        key=input("Enter key : ")
        value=input("Enter value : ")
        try:
            d[key] = float(value)
        except ValueError:
            pass
    s=0
    for i in d:
        s=s+d[i]
    print("Sum =",s)
except:
    print("Some error occured")

    
    