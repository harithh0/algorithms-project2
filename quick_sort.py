def quicksort(arr: list[int]):
    if (len(arr) < 2):
        return arr
    else:
        less_than: list[int] = []
        greater_than: list[int] = []
        same_value: list[int] = []
        pivot: int = arr[0]
        for i in arr[1:]:
            if i < pivot:
                less_than.append(i)
            elif i > pivot:
                greater_than.append(i)
            else:
                same_value.append(i)

        return quicksort(less_than) + same_value + [pivot
                                                    ] + quicksort(greater_than)
