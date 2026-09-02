# 2. Create two threads, one printing even numbers and the other printing odd numbers
# from 1 to 10. Ensure proper synchronization to alternate between even and odd
# numbers.

import threading

lock = threading.Lock()

def odd():
    for i in range(1, 11, 2):
        lock.acquire()
        print(i)
        lock.release()

def even():
    for i in range(2, 11, 2):
        lock.acquire()
        print(i)
        lock.release()

t1 = threading.Thread(target=odd)
t2 = threading.Thread(target=even)

t1.start()
t2.start()

t1.join()
t2.join()