def another_function():
    print("Hello world")


# temp 2
def sorter2(arr):
    # this is a modified version of the sorter
    print("codeflash stdout: Sorting list")
    if len(arr) > 1:
        arr.sort()
    print(f"result: {arr}")
    return arr


def sorter(arr):
    print("codeflash stdout: Sorting list")
    arr.sort()
    print(f"result: {arr}")
    return arr

