def counting_sort(arr, exp):
    # Sorts numbers based on the digit at the given exponent (exp)
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # For digits 0-9

    # Count occurrences of digits at current place value
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Compute cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the sorted output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy sorted elements back to original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    #Sorts an array using Radix Sort
    max_num = max(arr)  # Find the max number to determine number of digits
    exp = 1  # Start with the least significant digit (1s place)
    
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to the next place value

    sorted_arr= radix_sort(arr)
    print("Sorted array:", sorted_arr)
