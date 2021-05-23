import numpy as np
from autograd import grad

def simple_gradient_descent(f, x0, lr=1e-03, patience=10,  threshold=1e-05, final_lr=1e-07):
    derivative_fn = grad(f)
    iter = 0
    min_fx = 1000000
    waiting = 0
    iter = 0
    while True:
        fx = f(x0)
        x0 -= lr * derivative_fn(x0)
        if min_fx - fx > threshold:
            min_fx = fx
            waiting = 0
        elif waiting > patience:
            lr = lr / 3
            waiting = 0
            if lr < final_lr:
                break
        print(f'Iter: {iter} x: {x0} fx: {fx} lr: {lr}')
        waiting += 1
        iter += 1