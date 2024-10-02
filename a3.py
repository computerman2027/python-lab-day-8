details={}
print("To Stop input press key as 0")
while(True):
    key=input("Enter key : ")
    if (key.isdigit()):
        try:
            if(int(key)==0):
                break
        except:
            pass
    value=input("Enter value : ")
    if key not in details:
        details[key]=value
print("Detains entered :",details)