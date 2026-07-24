# 1. Python Program to Add a Key-Value Pair to the Dictionary

def add_key_value_pair(dictionary, key, value):
    dictionary[key] = value
    return dictionary   



my_dict = {'name': 'Alice', 'age': 25}      
new_key =input('enter key:')
new_value = input('enter value:')

updated_dict = add_key_value_pair(my_dict, new_key, new_value)
print(updated_dict) 