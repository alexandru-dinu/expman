import subprocess


def get_first_available_gpu() -> int:
    """Find first GPU with 0 memory usage. exit(1) if no GPU could be found."""
    result = subprocess.check_output(
        ["nvidia-smi", "--query-gpu=memory.used", "--format=csv,nounits,noheader"],
        encoding="utf-8",
    )
    usage = [int(x) for x in result.strip().split("\n")]

    try:
        first_available = usage.index(0)
    except ValueError:
        print("No GPU with 0 memory usage found!")
        exit(1)

    return first_available
