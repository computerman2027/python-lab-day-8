dict={'a':100, 'b':200, 'c':300}
key=input("enter a key:")
if dict.has_key(key):
    print("Present, value = ",dict[key])
else:
    print("Not Present")

enter a key:a
Traceback (most recent call last):
  File "C:/38_cse1/day 7/p29.py", line 3, in <module>
    if dict.has_key(key):
AttributeError: 'dict' object has no attribute 'has_key'
