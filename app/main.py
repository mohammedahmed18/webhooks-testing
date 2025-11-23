def sorter(arr):
    print("codeflash stdout: Sorting list")
    arr.sort()
    print(f"result: {arr}")
    return arr


def bubble_sort_4(arr1):
    n = len(arr1)
    for i in range(n):
        did_swapped = False
        for j in range(0, n - i - 1):
            if arr1[j] > arr1[j + 1]:
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
                did_swapped = True
        if not did_swapped:
            break

    return arr1


def bubble_sort_new_77(arr1):
    n = len(arr1)
    for i in range(n):
        did_swapped = False
        bound = n - i - 1
        for j in range(bound):
            a = arr1[j]
            b = arr1[j + 1]
            if a > b:
                arr1[j], arr1[j + 1] = b, a
                did_swapped = True
        if not did_swapped:
            break
    return arr1

