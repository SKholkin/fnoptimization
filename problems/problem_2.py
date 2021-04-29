import numpy as np

x0 = np.array([-1.2, -1])
eps = 1e-07

def f(x):
    assert x.size == 2, "Function input vector doesn't matches function dim"
    return 100 * np.square(x[1] - x[1] ** 3) + np.square(1 - x[0])
