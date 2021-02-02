import matplotlib.pyplot as plt
import numpy as np

from unit8 import delay_embedding


def cover_boxes(dat, eps=0.5):
    # this step is not necessary
    # keeping to be consistent with the lectures
    dat = dat - dat.min(axis=0)

    indices = np.ceil(dat / eps)
    indices = np.unique(indices, axis=0)
    n_boxes = indices.shape[0]  # N(eps)
    return n_boxes


def plot_dimension_capacity(dat):
    eps_range = 10 ** np.linspace(-1.5, 2, num=100)
    n_boxes = [cover_boxes(dat=dat, eps=eps) for eps in eps_range]
    e_min, e_max = 40, 85
    e_log_inv = np.log(1 / eps_range[e_min: e_max])
    deg = np.polyfit(x=e_log_inv, y=np.log(n_boxes[e_min: e_max]), deg=1)

    plt.plot(1 / eps_range, n_boxes)
    plt.vlines(x=1 / eps_range[[e_min, e_max]], ymin=min(n_boxes),
               ymax=max(n_boxes), ls='--', color='black', lw=1)
    plt.plot(1 / eps_range[e_min: e_max], np.e ** np.polyval(deg, x=e_log_inv))
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel(r"$\log(1 / \epsilon)$")
    plt.ylabel(r"$\log \thinspace N(\epsilon)$")
    plt.title(f"Dimension capacity: {deg[1]:.2f}")
    plt.show()


if __name__ == '__main__':
    data = np.loadtxt("amplitude.dat")
    data = delay_embedding(data, T=8, m=2)
    print(cover_boxes(data, eps=0.5))
    quit()
    data = np.loadtxt("CapDimData.dat", delimiter=',')
    print(f"{data.shape=}")
    print(f"{cover_boxes(data[:, [0, 2]], eps=0.05)=}")
    print(f"{cover_boxes(data[:, [0, 2]], eps=0.5)=}")
    plot_dimension_capacity(data)
