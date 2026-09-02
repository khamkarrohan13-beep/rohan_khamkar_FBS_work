# 3. Implement two threads to print lowercase and uppercase alphabets concurrently from
# 'a' to 'z' and 'A' to 'Z'.

import threading

def lowercase():
    for i in "abcdefghijklmnopqrstuvwxyz":
        print(i, end=" ")

def uppercase():
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(i, end=" ")

t1 = threading.Thread(target=lowercase)
t2 = threading.Thread(target=uppercase)

t1.start()
t2.start()

t1.join()
t2.join()