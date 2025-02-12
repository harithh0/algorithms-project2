import time 
from bubblesort import bubble_sort
from test_data import hundred_best

start = time.time()
bubble_sort(hundred_best)
stop = time.time()
print(stop-start)