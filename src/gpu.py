import subprocess
from typing import Optional

import numpy as np


def get_first_available_gpu_id(limit: int) -> Optional[int]:
    """
    Returns the ID of the first GPU with memory usage <= limit
    or None if no GPU could be found.
    """
    result = subprocess.check_output(
        ["nvidia-smi", "--query-gpu=memory.used", "--format=csv,nounits,noheader"],
        encoding="utf-8",
    )
    usage = np.array([int(x) for x in result.strip().split("\n")])

    try:
        return sorted(np.where(usage <= limit)[0])[0]
    except ValueError:
        print("No GPU with 0 memory usage found!")
        return None


if __name__ == "__main__":
    print(get_first_available_gpu_id(limit=128))
