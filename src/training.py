import math


def get_cosine_learning_rates(lr_min: float, lr_max: float, f: float, N: int):
    """Decay the learning rate based on a cosine schedule.
    Return a list of `N` learning rate values in the interval `[lr_min, lr_max]`, with frequency `f`.
    """
    lr = []

    for i in range(N):
        freq = f * i / N
        scaler = 0.5 * (1 + math.cos(2 * math.pi * freq))  # [0, 1]
        l = lr_min + scaler * (lr_max - lr_min)
        lr.append(l)

    return lr


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    lrs = get_cosine_learning_rates(lr_min=1e-5, lr_max=1e-3, f=2, N=100)

    plt.plot(lrs, linestyle="--", marker=".")
    plt.savefig("/tmp/lr.png")
