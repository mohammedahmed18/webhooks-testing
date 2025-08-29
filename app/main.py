def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort5(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr




def bubble_sort_new(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        bound = n - i - 1
        for j in range(bound):
            a = arr[j]
            b = arr[j + 1]
            if a > b:
                arr[j], arr[j + 1] = b, a
                swapped = True
        if not swapped:
            break
    return arr
