import random


def quicksort(arr: list[int]):
    if len(arr) < 2:
        return arr
    else:
        less_than: list[int] = []
        greater_than: list[int] = []
        same_value: list[int] = []
        pivot: int = arr[0]  # -- bad - causes imbalance
        # pivot: int = arr[random.randint(0, len(arr) - 1)]  # much better
        for i in arr:
            if i < pivot:
                less_than.append(i)
            elif i > pivot:
                greater_than.append(i)
            else:
                same_value.append(i)

        return quicksort(less_than) + same_value + quicksort(greater_than)


if __name__ == "__main__":
    from test_data import tenThousand_worst

    a = quicksort(tenThousand_worst)
    print(a)
