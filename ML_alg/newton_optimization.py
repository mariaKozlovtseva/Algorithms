import numpy as np

def total_error(params):
    total_error = 0
    n = x.shape[0]
    for i in range(n):
        x_i = x[i]
        y_i = y[i]
        total_error += np.square((y_i - (x_i.dot(params[:-1]) + params[-1])))
    return total_error / n

def compute_jacobian(params, h = 1e-5):
    n = len(params)
    jacobian = np.zeros(n)
    for i in range(n):
        x_i = np.zeros(n)
        x_i[i] += h
        jacobian[i] = (total_error(params + x_i) - total_error(params)) / h
    return jacobian

def compute_hessian(params, h=1e-5):
    n = len(params)
    hessian = np.zeros((n, n))
    for i in range(n):
        x_i = np.zeros(n)
        x_i[i] += h
        hessian[i] = (compute_jacobian(params + x_i) - compute_jacobian(params)) / h
    return hessian

def newton_optimization(init_pair, max_iter = 1000, tol = 1e-5, verbose=True):
    points_pair_arr = np.zeros((max_iter, len(init_pair)))
    points_pair_arr[0] = init_pair
    opt_val = None
    for i in range(max_iter):
        jacob = compute_jacobian(points_pair_arr[i])
        hessian = compute_hessian(points_pair_arr[i])
        points_pair_arr[i + 1] = points_pair_arr[i] - np.dot(np.linalg.pinv(hessian), jacob)
        if verbose:
            print('On %d iteration m_hats are %.2f and b_hat is %.2f' % (
            i, points_pair_arr[i, 0], points_pair_arr[i, 1]))
        opt_val = points_pair_arr[i+1]
        min_mse = min(total_error(points_pair_arr[j]) for j in range(i + 1))

        if np.abs(total_error(points_pair_arr[i]) - total_error(points_pair_arr[i + 1])) < tol:
            break
    return opt_val, min_mse

if __name__ == '__main__':
    x = np.random.randn(1000, 1)
    # make 2 features: x^2 and x
    x = np.column_stack((np.square(x), x))
    # params
    m = np.array([[3.], [-2.]])
    b = np.array([[0.5] * len(x)]).T
    y = x.dot(m) + b
    # testing
    import time

    init_points = np.zeros(3)  # 3 params: m1, m2 and b
    time_start = time.time()
    newton_points, mse = newton_optimization(init_points, max_iter=100)
    # as you'll see it took us only 2 iterations to train
    # and estimated params are pretty close to true ones
    print('m1_hat: {}, m2_hat: {}, b_hat: {}'.format(*newton_points))
    print('MSE: %.2f' % mse)
    print('Time: %f' % (time.time() - time_start))
    # plot results
    import matplotlib.pyplot as plt
    y_hat = x.dot(newton_points[:-1]) + newton_points[-1]
    plt.scatter(x[:, 1], y, label='True graph')
    plt.scatter(x[:, 1], y_hat, label='Approximated graph')
    plt.legend()