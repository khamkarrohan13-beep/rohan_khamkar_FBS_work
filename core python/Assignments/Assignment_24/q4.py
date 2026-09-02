# 4. Implement a producer-consumer problem with a limited buffer of size 5. Create two
# producer threads and two consumer threads. Producers produce items, and consumers
# consume them. Ensure proper synchronization to avoid buffer overflows or underflows.


import threading
import time

buffer = []

empty = threading.Semaphore(5)
full = threading.Semaphore(0)
lock = threading.Lock()


def producer(name):
    for i in range(5):
        empty.acquire()

        lock.acquire()
        buffer.append(i)
        print(name, "produced", i)
        lock.release()

        full.release()
        time.sleep(0.1)


def consumer(name):
    for i in range(5):
        full.acquire()

        lock.acquire()
        item = buffer.pop(0)
        print(name, "consumed", item)
        lock.release()

        empty.release()
        time.sleep(0.1)


p1 = threading.Thread(target=producer, args=("Producer 1",))
p2 = threading.Thread(target=producer, args=("Producer 2",))

c1 = threading.Thread(target=consumer, args=("Consumer 1",))
c2 = threading.Thread(target=consumer, args=("Consumer 2",))

p1.start()
p2.start()
c1.start()
c2.start()

p1.join()
p2.join()
c1.join()
c2.join()