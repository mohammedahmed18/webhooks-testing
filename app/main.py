from app.utils import swap


def sorter_test_final8(arr):
    print("codeflash stdout: Sorting list")
    arr.sort()
    print(f"result: {arr}")
    return arr


def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(n):
        swapped = False
        # After each i-th pass, the last i elements are in sorted position
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # use Pythonic tuple swap for efficiency
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            # No swaps means array is already sorted
            break
    print(f"result: {arr}")
    return arr
