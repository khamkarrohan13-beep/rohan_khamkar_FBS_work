# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

def check_key_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False    
    
d1 = {'name': 'rohan', 'age': 25, 'city': 'pune'}
key_to_check = input('enter key to check:')


result = check_key_exists(d1, key_to_check)
print(result) 
