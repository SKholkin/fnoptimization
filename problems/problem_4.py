import numpy as np

x0 = np.array([3, -1, 0, 1])
eps = 1e-07

def f(x):
    assert x.size == 4, "Function input vector doesn't matches function dim"
    return (x[0] + 10 * x[1]) ** 2 + 5* (x[2] - x[3]) ** 2 + (x[1] - 2 * x[2]) ** 4 + 10 * (x[0] - x[3]) ** 4
