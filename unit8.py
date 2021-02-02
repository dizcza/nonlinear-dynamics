import numpy as np
import matplotlib.pyplot as plt


def delay_embedding(dat, T, m):
    n = len(dat) - (m - 1) * (T + 1) + 1
    jj = np.arange(m) * T
    ii = np.arange(n)
    indices = np.expand_dims(ii, axis=1) + jj
    reconstructed = dat[indices]
    print(f"{reconstructed.shape=}")
    return reconstructed


def plot_embedding(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, lw=0.1)
    plt.show()


if __name__ == '__main__':
    data = np.loadtxt('amplitude.dat', dtype=np.float32)
    rec = delay_embedding(data, T=1, m=7)
    plot_embedding(rec[:, 0], rec[:, 2])
