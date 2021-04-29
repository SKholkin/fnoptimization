import numpy as np
from functools import reduce

# Метод Нелдера Мида (Nelder-Mead method)

def init_simplex(x0, init_eps=1e-01):
    simplex = [x0]
    for dim, x in enumerate(x0):
        x_new = x0.copy()
        x_new[dim] = x + init_eps
        simplex.append(x_new)
    return simplex

def calculate_centroid(simplex):
    return 1 / (len(simplex)) *  reduce(lambda a, b: a + b['x'], simplex, np.zeros(simplex[0]['x'].shape))

def shrink_simplex(simplex, center, f, sigma=0.5):
    new_simplex = [{'x': center + sigma * (item['x'] - center),
     'fx': f(center + sigma * (item['x'] - center))}
      for item in simplex]
    return new_simplex

def nelder_mead_method(f, x0, a=1, b=0.5, gamma=2, sigma=0.5, eps=1e-03, init_simplex_eps=1e-01, verbose=False):
    """
    a: reflection coef
    b: contradiction coef
    gamma: expansion coef
    sigma: shrink (global shrink) coef
    """
    simplex = init_simplex(x0, init_eps=init_simplex_eps)
    simplex = [{'x': x, 'fx': f(x)} for x in simplex]
    simplex = sorted(simplex, key=lambda item: item['fx'], reverse=True)
    print(simplex)
    delta = 2 * eps
    iter = 0
    while delta > eps:
        xh_point = simplex[0]
        xg_point = simplex[1]
        xl_point = simplex[-1]
        xc_point = {'x': calculate_centroid(simplex[1:]), 'fx': f(calculate_centroid(simplex[1:]))}
        # reflection
        xr_point = {'x': (1 + a) * xc_point['x'] - a * xh_point['x'],
         'fx': f((1 + a) * xc_point['x'] - a * xh_point['x'])}
        if xr_point['fx'] < xl_point['fx']:
            # expansion
            xe_point = {'x': (1 - gamma) * xc_point['x'] +  gamma * xr_point['x'],
             'fx': f((1 - gamma) * xc_point['x'] +  gamma * xr_point['x'])}
            if xe_point['fx'] < xr_point['fx']:
                xh_point['x'] = xe_point['x']
                xh_point['fx'] = xe_point['fx']
            else: 
                xh_point['x'] = xr_point['x']
                xh_point['fx'] = xr_point['fx']
        elif xl_point['fx'] < xr_point['fx'] and xr_point['fx'] < xg_point['fx']:
            xh_point['x'] = xr_point['x']
            xh_point['fx'] = xr_point['fx']
        else:
            if xg_point['fx'] < xr_point['fx'] and xr_point['fx'] < xh_point['fx']:
                temp = {'x': xh_point['x'], 'fx': xh_point['fx']}
                xh_point['x'] = xr_point['x']
                xh_point['fx'] = xr_point['fx']
                xr_point['x'] = temp['x']
                xr_point['fx'] = temp['fx']
            # condradiction
            xs_point = {'x': b * xh_point['x'] + (1 - b) * xc_point['x'],
            'fx': f(b * xh_point['x'] + (1 - b) * xc_point['x'])}
            if xs_point['fx'] < xh_point['fx']:
                xh_point['x'] = xs_point['x']
                xh_point['fx'] = xs_point['fx']
            else:
                # shrink
                simplex = shrink_simplex(simplex, xl_point['x'], f, sigma=sigma)
        # calculate delta
        delta = np.mean(np.var(np.array([item['x'] for item in simplex]), axis=0))
        # ToDo: do not sort
        simplex = sorted(simplex, key=lambda item: item['fx'], reverse=True)
        iter += 1
        print(f"Iter: {iter} x: {simplex[-1]['x']} fx: {simplex[-1]['fx']} delta: {delta}")
    
