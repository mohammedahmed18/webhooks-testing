from app.utils import swap


def sorter_test_final6(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    # Use bubble sort with early exit if no swaps were made in a pass
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Use Python's fast tuple unpacking to swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    print(f"result: {arr}")
    return arr


def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = swap(arr[j], arr[j + 1])
    print(f"result: {arr}")
    return arr
