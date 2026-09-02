# 1. Calculate the sum of squares of numbers from 1 to 100 using four threads. Divide the
# range equally among the threads, and each thread calculates the sum of squares for its
# range. Finally, combine the results to get the total sum of squares.

import threading as td

result = [0, 0, 0, 0]

def sum_of_squares(start, end, index):
    total = 0

    for i in range(start, end + 1):
        total += i * i

    result[index] = total


t1 = td.Thread(target=sum_of_squares, args=(1, 25, 0))
t2 = td.Thread(target=sum_of_squares, args=(26, 50, 1))
t3 = td.Thread(target=sum_of_squares, args=(51, 75, 2))
t4 = td.Thread(target=sum_of_squares, args=(76, 100, 3))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

total = sum(result)

print("Sum of squares from 1 to 100 =", total)