import time
from datetime import datetime

def sorter(arr):
    print("codeflash stdout: Sorting list")
    arr.sort()
    print(f"result: {arr}")
    return arr


def generate_timestamped_id(prefix: str = "id") -> str:
    """Generate an ID with a timestamp and random component."""
    timestamp = int(time.time())
    return f"{prefix}_{timestamp}"
