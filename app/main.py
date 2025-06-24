import time
from datetime import datetime

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


def generate_timestamped_id(prefix: str = "id") -> str:
    """Generate an ID with a timestamp and random component."""
    timestamp = int(time.time())
    return f"{prefix}_{timestamp}"
