import time
from datetime import datetime

def sorter(arr):
    print("codeflash stdout: Sorting list")
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]  # Shift, no swap
            j -= 1
        arr[j + 1] = x  # Insert element
    print(f"result: {arr}")
    return arr


def generate_timestamped_id(prefix: str = "id") -> str:
    """Generate an ID with a timestamp and random component."""
    timestamp = int(time.time())
    return f"{prefix}_{timestamp}"
