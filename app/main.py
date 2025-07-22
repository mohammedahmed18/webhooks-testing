from app.utils import swap


def sorter_test_final4(arr):
    print("codeflash stdout: Sorting list")
    arr.sort()
    print(f"result: {arr}")
    return arr


def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):  # Reduce by i since last i elements are in place
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = (
                    arr[j + 1],
                    arr[j],
                )  # In-place tuple swap (fast in Python)
                swapped = True
        if not swapped:
            break  # List is already sorted
    print(f"result: {arr}")
    return arr
