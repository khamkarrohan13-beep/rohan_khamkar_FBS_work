# 3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def my_range(start,stop,step):
    while start < stop:
        yield start
        start=start + step

start=int(input('enter start: '))    
stop=int(input('enter stop: '))    
step=int(input('enter step: '))    

for i in my_range(start,stop,step):
    print(i)