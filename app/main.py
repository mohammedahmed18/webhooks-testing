def sorter_test(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # direct swap, faster
                swapped = True
        if not swapped:
            break  # stop early if no swaps occurred (already sorted)
    print(f"result: {arr}")
    return arr


def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    # Use efficient built-in sort instead of Bubble Sort
    arr.sort()
    print(f"result: {arr}")
    return arr
