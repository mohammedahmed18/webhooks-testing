from app.utils import swap


def sorter_test2(arr):
    print("codeflash stdout: Sorting list")
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    print(f"result: {arr}")
    return arr


def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):  # Each pass, skip the sorted largest elements
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # use fast python swap, inline
                swapped = True
        if not swapped:
            break  # Exit early if already sorted
    print(f"result: {arr}")
    return arr
