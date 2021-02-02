import matplotlib.pyplot as plt
import numpy as np


def logistic_map(x0, r, n):
    xs = [x0]
    x = x0
    for i in range(n):
        x = r * x * (1 - x)
        xs.append(x)
    return xs


def bifurcation_diagram(x0, r_min, r_max, r_step, n, k):
    fig, ax = plt.subplots()
    r_range = np.arange(r_min, r_max + r_step, r_step)
    cycles = {}
    for r in r_range:
        xs = logistic_map(x0=x0, r=r, n=n)[k:]
        xs = np.unique(xs)
        cycles[r] = len(xs)
        ax.scatter(np.full_like(xs, r), xs, c='b', s=r_step)
    return cycles


if __name__ == '__main__':
    # bifurcation_diagram(x0=0.2, r_min=2.8, r_max=3.9, r_step=0.01, n=1000, k=50)
    bifurcation_diagram(x0=0.5, r_min=3.84, r_max=3.8571, r_step=0.001, n=1000, k=50)
    plt.show()
