tuplex=tuple("ipndex tuple")
print(tuplex)

index=tuplex.index("p")
print(index)

index=tuplex.index("p",5)
print(index)

index=tuplex.index("e",3,6)
print(index)

index=tuplex.index("y")




#('i', 'p', 'n', 'd', 'e', 'x', ' ', 't', 'u', 'p', 'l', 'e')
#1
#9
#4
#Traceback (most recent call last):
#  File "C:/38_cse1/day 7/p9.py", line 13, in <module>
#    index=tuplex.index("y")
#ValueError: tuple.index(x): x not in tuple
