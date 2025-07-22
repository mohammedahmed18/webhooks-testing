from app.utils import swap


def sorter_test_final3(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(n):
        swapped = False  # Early exit if no swaps
        # Optimization: after i passes, the last i elements are sorted
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Use fast tuple swap rather than function call
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
