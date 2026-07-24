# 2. Python Program to Concatenate Two Dictionaries Into One

def concatenate_dicts(dict1, dict2):
    return dict1 | dict2  

dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'pune', 'country': 'India'}        
    
concatenated_dict = concatenate_dicts(dict1, dict2)
print(concatenated_dict)      



#method 2
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d1.update(d2)
print(d1) 