def sorter_lts(arr):
    print("codeflash stdout: Sorting list")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                swap(arr[j], arr[j + 1])
    print(f"result: {arr}")
    return arr


def swap(val1, val2):
    temp = val1
    val1 = val2
    val2 = temp
    return (val1, val2)

def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                swap(arr[j], arr[j + 1])
    print(f"result: {arr}")
    return arr

