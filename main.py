import time 
from bubblesort import bubble_sort

with open('100.txt') as f:
    number_list = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            number_list.append(line)

start = time.time()
bubble_sort(number_list)
stop = time.time()
print(stop-start)