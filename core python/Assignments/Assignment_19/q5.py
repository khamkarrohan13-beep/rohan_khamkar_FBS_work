# 5. Find all of the words in a string that are less than 5 letters (take
# input from user)

string=input('enter a string:')

result=[i for i in string.split() if len(i)<5]


print("Words having less than 5 letters:", result)