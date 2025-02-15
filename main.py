import time

from bubblesort import bubble_sort
from mergesort import merge_sort
from quick_sort import quicksort
from radixsort import radix_sort
from test_data import *

CLOSE = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"

# Best case data
best_cases = [{
    "name": "hundred_best",
    "data": hundred_best
}, {
              "name": "thousand_best",
              "data": thousand_best
              }, {
              "name": "tenThousand_best",
              "data": tenThousand_best
              }]

# Average case data
avg_cases = [{
    "name": "hundred_avg",
    "data": hundred_avg
}, {
             "name": "thousand_avg",
             "data": thousand_avg
             }, {
             "name": "tenThousand_avg",
             "data": tenThousand_avg
             }]

# Worst case data
worst_cases = [{
    "name": "hundred_worst",
    "data": hundred_worst
}, {
               "name": "thousand_worst",
               "data": thousand_worst
               }, {
               "name": "tenThousand_worst",
               "data": tenThousand_worst
               }]


def measure_worst(**functions):
    print(f"{BLUE}Testing Worst Time O{CLOSE}")

    for case in worst_cases:
        for function_name, function in functions.items():
            print(f"{GREEN}Testing {function_name} for {str(case.get("name"))}...{CLOSE}")
            start = time.perf_counter()
            function(case.get("data"))
            stop = time.perf_counter()
            elapsed_micro = (stop - start) * 1_000_000
            elapsed_seconds = (stop - start)
            print(f"took {elapsed_micro} microseconds")
            print(f"took {elapsed_seconds} seconds\n")


def measure_average(**functions):
    print(f"{BLUE}Testing Average Time Θ{CLOSE}")
    for case in avg_cases:
        for function_name, function in functions.items():
            print(f"{GREEN}Testing {function_name} for {str(case.get("name"))}...{CLOSE}")
            start = time.perf_counter()
            function(case.get("data"))
            stop = time.perf_counter()
            elapsed_micro = (stop - start) * 1_000_000
            elapsed_seconds = (stop - start)
            print(f"took {elapsed_micro} microseconds")
            print(f"took {elapsed_seconds} seconds\n")


def measure_best(**functions):
    print(f"{BLUE}Testing Best Time Ω{ CLOSE}")
    for case in best_cases:
        for function_name, function in functions.items():
            print(f"{GREEN}Testing {function_name} for {str(case.get("name"))}...{CLOSE}")
            start = time.perf_counter()
            function(case.get("data"))
            stop = time.perf_counter()
            elapsed_micro = (stop - start) * 1_000_000
            elapsed_seconds = (stop - start)
            print(f"took {elapsed_micro} microseconds")
            print(f"took {elapsed_seconds} seconds\n")



def main():
    # add algorithms here
    functions_dict = {
        "bubble": bubble_sort,
        "quicksort": quicksort,
        "merge_sort": merge_sort,
    # "radixsort": radix_sort

    }
    measure_worst(**functions_dict)
    measure_average(**functions_dict)
    measure_best(**functions_dict)


if __name__ == "__main__":
    main()
