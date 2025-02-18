import copy
import time

import pandas as pd

from bubblesort import bubble_sort
from mergesort import merge_sort
from quick_sort import quicksort
from radixsort import radix_sort
from test_data import *

# Initialize a dictionary to store time data
time_data = {"Algorithm": [], "Size": [], "Case": [], "Time (seconds)": []}
CLOSE = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"

# Best case data
best_cases = [
    {
        "name": "hundred_best",
        "data": hundred_best
    },
    {
        "name": "thousand_best",
        "data": thousand_best
    },
    {
        "name": "tenThousand_best",
        "data": tenThousand_best
    },
]

# Average case data
avg_cases = [
    {
        "name": "hundred_avg",
        "data": hundred_avg
    },
    {
        "name": "thousand_avg",
        "data": thousand_avg
    },
    {
        "name": "tenThousand_avg",
        "data": tenThousand_avg
    },
]

# Worst case data
worst_cases = [
    {
        "name": "hundred_worst",
        "data": hundred_worst
    },
    {
        "name": "thousand_worst",
        "data": thousand_worst
    },
    {
        "name": "tenThousand_worst",
        "data": tenThousand_worst
    },
]


# Modify the measure functions to collect data
def measure_worst(**functions):
    print(f"{BLUE}Testing Worst Time O{CLOSE}")
    for case in worst_cases:
        for function_name, function in functions.items():
            print(
                f"{GREEN}Testing {function_name} for {str(case.get('name'))}...{CLOSE}"
            )
            start = time.perf_counter()
            function(case.get("data"))
            stop = time.perf_counter()
            elapsed_seconds = stop - start
            print(f"took {elapsed_seconds} seconds\n")

            # Collect data
            time_data["Algorithm"].append(function_name)
            time_data["Size"].append(case.get("name"))
            time_data["Case"].append("Worst")
            time_data["Time (seconds)"].append(elapsed_seconds)


def measure_average(**functions):
    print(f"{BLUE}Testing Average Time Θ{CLOSE}")
    for case in avg_cases:
        for function_name, function in functions.items():
            print(
                f"{GREEN}Testing {function_name} for {str(case.get('name'))}...{CLOSE}"
            )
            start = time.perf_counter()
            function(case.get("data"))
            stop = time.perf_counter()
            elapsed_seconds = stop - start
            print(f"took {elapsed_seconds} seconds\n")

            # Collect data
            time_data["Algorithm"].append(function_name)
            time_data["Size"].append(case.get("name"))
            time_data["Case"].append("Average")
            time_data["Time (seconds)"].append(elapsed_seconds)


def measure_best(**functions):
    print(f"{BLUE}Testing Best Time Ω{CLOSE}")
    for case in best_cases:
        for function_name, function in functions.items():
            print(
                f"{GREEN}Testing {function_name} for {str(case.get('name'))}...{CLOSE}"
            )
            start = time.perf_counter()
            function(case.get("data"))
            stop = time.perf_counter()
            elapsed_seconds = stop - start
            print(f"took {elapsed_seconds} seconds\n")

            # Collect data
            time_data["Algorithm"].append(function_name)
            time_data["Size"].append(case.get("name"))
            time_data["Case"].append("Best")
            time_data["Time (seconds)"].append(elapsed_seconds)


# save data as csv
def save_to_csv():
    # Convert the time data dictionary to a DataFrame
    df = pd.DataFrame(time_data)

    # Define the custom path
    file_path = r"C:\Users\sorting_algorithm_times.csv"

    # Save the DataFrame as a CSV file
    df.to_csv(file_path, index=False)
    print(f"CSV file saved at: {file_path}")


def test_all_algorithms():
    # for testing only
    # add algorithms here
    functions_dict = {
        "bubble": bubble_sort,
        "quicksort": quicksort,
        "merge_sort": merge_sort,
        "radixsort": radix_sort,
    }
    measure_worst(**functions_dict)
    measure_average(**functions_dict)
    measure_best(**functions_dict)

    # Save the time data to CSV
    save_to_csv()


def test_algorithm(func, complexity: str, chosen_data: list[dict]):
    # for user i/o
    print(f"In {complexity} case,")
    for case in chosen_data:
        temp_data = copy.deepcopy(case.get("data"))
        start = time.perf_counter()
        func(temp_data)
        stop = time.perf_counter()
        elapsed_seconds = stop - start
        print(f"N={case.get('name')} took {elapsed_seconds:.6f} seconds\n")

    while True:
        users_other_n_chose = str(
            input("Do you want to input another N (Y/N)? "))
        if users_other_n_chose.lower() == "y":
            n_amount = int(input("What is the N? "))
            if complexity == "best":
                list_of_n_amount = list(range(0, n_amount))
            elif complexity == "average":
                half = n_amount // 2
                first_half = list(range(0, half))
                second_half = list(range((half * 2) - 1, half - 1, -1))
                list_of_n_amount = first_half + second_half
            elif complexity == "worst":
                list_of_n_amount = list(range(n_amount, 0, -1))
            else:
                exit()
            start = time.perf_counter()
            func(list_of_n_amount)
            stop = time.perf_counter()
            elapsed_seconds = stop - start
            print(f"N={n_amount} took {elapsed_seconds:.6f} seconds\n")
        else:
            break


def selection(algorithm):
    algorithm_name = algorithm.get("name")
    algorithm_function = algorithm.get("function")
    print(f"""
    Case scenarios for {algorithm_name}
    ---------------
    1. best case
    2. average case
    3. worst case
    4. exit {algorithm_name} test""")

    userchoice = int(input("Select the case (1-4): "))
    if userchoice == 1:
        test_algorithm(algorithm_function, "best", best_cases)
    elif userchoice == 2:
        test_algorithm(algorithm_function, "average", avg_cases)
    elif userchoice == 3:
        test_algorithm(algorithm_function, "worst", worst_cases)
    elif userchoice == 4:
        return


def main():
    algorithms = [
        {
            "name": "Bubble Sort",
            "function": bubble_sort
        },
        {
            "name": "Merge Sort",
            "function": merge_sort
        },
        {
            "name": "Quick Sort",
            "function": quicksort
        },
        {
            "name": "Radix Sort",
            "function": radix_sort
        },
    ]
    # i/o
    finished = False
    while not finished:
        print("Welcome to the test suite of selected sorting algorithms!")
        print("""
    Select the sorting algorithm you want to test.
    -------------------------
    1. Bubble Sort
    2. Merge Sort
    3. Quick Sort
    4. Radix Sort
    5. Exit""")

        userchoice = int(input("Select a sorting algorithm (1-5): "))

        if userchoice == 1:
            selection(algorithms[0])
        elif userchoice == 2:
            selection(algorithms[1])
            pass
        elif userchoice == 3:
            selection(algorithms[2])
            pass
        elif userchoice == 4:
            selection(algorithms[3])
        elif userchoice == 5:
            finished = True
            print("bye!")


if __name__ == "__main__":
    main()  # for user I/O
    # test_all_algorithms() # for time analysis testing
