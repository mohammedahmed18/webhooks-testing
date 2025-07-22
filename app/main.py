from app.utils import swap

def sorter_test_final7(arr):
    print("codeflash stdout: Sorting list")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = swap(arr[j], arr[j + 1])
    print(f"result: {arr}")
    return arr


def sorter_lts2(arr):
    print("codeflash stdout: Sorting list")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = swap(arr[j], arr[j + 1])
    print(f"result: {arr}")
    return arr

