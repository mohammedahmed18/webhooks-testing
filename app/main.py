def sorter_test_final7(arr):
    print("codeflash stdout: Sorting list")
    arr.sort()
    print(f"result: {arr}")
    return arr


def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(n):
        swapped = False  # Early exit if no swaps in this pass
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Fastest way to swap values directly in Python
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    print(f"result: {arr}")
    return arr
