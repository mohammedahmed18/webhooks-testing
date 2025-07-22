from app.utils import swap


def sorter_test_final5(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
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
        swapped = False  # Early exit flag
        for j in range(n - i - 1):  # Skip sorted suffix
            if arr[j] > arr[j + 1]:
                # Use Python's efficient tuple assignment for swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # No swaps, list is sorted
    print(f"result: {arr}")
    return arr
