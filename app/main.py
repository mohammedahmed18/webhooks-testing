import time
from datetime import datetime

def sorter(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(n):
        swapped = False
        # Only need to go up to n-1-i on each pass
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # List already sorted, exit early
    print(f"result: {arr}")
    return arr


def generate_timestamped_id(prefix: str = "id") -> str:
    """Generate an ID with a timestamp and random component."""
    timestamp = int(time.time())
    return f"{prefix}_{timestamp}"
