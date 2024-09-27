my_dict={'x':500,'y':5874,'z':560}

key_max = max(my_dict.keys(),key=(lambda k:my_dict[k]))
key_min = min(my_dict.keys(),key=(lambda k:my_dict[k]))

print("Maximum value = ",my_dict[key_max])
print("Minimum value = ",my_dict[key_min])
