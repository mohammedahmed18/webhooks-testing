from app.utils import swap


def sorter_test_final2(arr):
    print("codeflash stdout: Sorting list")
    arr.sort()
    print(f"result: {arr}")
    return arr


def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    # Bubble sort with early exit and reduced inner loop range
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Direct Pythonic swap, preserves function signature and output
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Stop early if already sorted
    print(f"result: {arr}")
    return arr
