def swap(val1, val2):
    # create a helper function for this to count down the number of swaps happened
    temp = val1
    val1 = val2
    val2 = temp
    return (val1, val2)