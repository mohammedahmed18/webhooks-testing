def sorter_lts(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    # Improved with bubble sort with swap in-place and early exit
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):  # Don't touch sorted tail
            if arr[j] > arr[j + 1]:
                # Do in-place swap to minimize function and variable overhead
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # List is sorted early, exit
    print(f"result: {arr}")
    return arr


def swap(val1, val2):
    temp = val1
    val1 = val2
    val2 = temp
    return (val1, val2)


def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = swap(arr[j], arr[j + 1])
    print(f"result: {arr}")
    return arr
