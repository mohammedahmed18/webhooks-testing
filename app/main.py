import time
from datetime import datetime

def sorter(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):  # optimize passes, omit sorted tail
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # faster swap
                swapped = True
        if not swapped:  # Stop if already sorted
            break
    print(f"result: {arr}")
    return arr


def generate_timestamped_id(prefix: str = "id") -> str:
    """Generate an ID with a timestamp and random component."""
    timestamp = int(time.time())
    return f"{prefix}_{timestamp}"
