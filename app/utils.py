def swap2(val1, val2):
    # create a helper function for this to count down the number of swaps happened
    temp = val1
    val1 = val2
    val2 = temp
    return (val1, val2)


def sorter(arr):
    arr.sort()
    return arr

def sorter2(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr