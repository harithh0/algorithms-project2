import time

from bubblesort import bubble_sort
from quick_sort import quicksort
from test_data import hundred_best

#we need xrange for quick sort xrange is just length of the array
xrange = len(hundred_best)

start = time.time()
bubble_sort(hundred_best)
stop = time.time()
print(stop - start)
