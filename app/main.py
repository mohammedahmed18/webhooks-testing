def sorter(arr):
    print("codeflash stdout: Sorting list")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print(f"result: {arr}")
    return arr


def newFunc():
    print("codeflash stdout: This is a new function")
    # I added a line here
    return "This is a new function, then I modiefied this here"



def newFunc2():
    return "This is another new function"


