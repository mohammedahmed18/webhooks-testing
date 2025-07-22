from app.utils import swap


def sorter_test_final9(arr):
    print("codeflash stdout: Sorting list")
    arr.sort()
    print(f"result: {arr}")
    return arr


def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):  # avoid unnecessary passes
            if arr[j] > arr[j + 1]:
                # Direct swap without helper or temp variable
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Already sorted
    print(f"result: {arr}")
    return arr
