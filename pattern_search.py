import numpy as np

# Метод Хука-Дживса (Hooke-Jeeves, Pattern search)
def pattern_search(f, x0, h, l=2, step=2, eps=1e-07, verbose=False):
    iter = 0
    if verbose: 
        print("Pattern search start:...")
    min_fx = f(x0)
    threshold = 10
    without_improvement = 0
    while h > eps:
        x0_old = np.copy(x0)
        for i, x  in enumerate(x0):
            x0_hplus = np.copy(x0)
            x0_hminus = np.copy(x0)
            x0_hplus[i] = x + h
            x0_hminus[i] = x - h
            if f(x0_hplus) < f(x0_hminus) and f(x0_hplus) < f(x0):
                x0 = x0_hplus
            elif f(x0_hminus) < f(x0):
                x0 = x0_hminus

        x0 = x0_old + l * (x0 - x0_old)
        print(f'iter {iter}: x = {x0} f(x) = {f(x0)} h = {h}')
        if f(x0) < min_fx:
            min_fx  = f(x0)
            without_improvement = 0
        else:
            without_improvement += 1
        iter += 1
        if np.array_equal(x0, x0_old) or without_improvement > threshold:
            h = h / step
            l = l / step
            continue
