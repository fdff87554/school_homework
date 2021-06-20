from numpy import array, zeros, linalg, round


# # We will not use this function but use CubicSpline in scipy.interpolate
# # This function is natural cubic spline
# def cubic_spline(x, y):
#     """Interpolation using natural cubic splines.
#
#     The natural cubic spline S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i) ** 2 + d_i(x - x_i) ** 3
#     a_i = f(x_i) = y_i
#     b_i = (1 / h_i) * (a_{i+1} - a_i) - (h_i / 3) * (c_{i+i} + 2 * c_{i})
#     d_i = (c_{i+1} - c_i) / (3 * h_i)
#     v_i = h_{i-1} * c_{i-i} + u_i * c_i + h_i * c_{i+1} = 3 * (w_i - w_{i-1})
#     w_i = (1/h_i) * (a_{i+1} - a_i)
#     u_i = 2 * (h_{i-1} + h_i)
#     h_i = x_{i+1} - x_i
#     """
#
#     x, y = array(x), array(y)
#     a = y
#     v = zeros(x.shape)
#     h = round([x[i + 1] - x[i] for i in range(len(x) - 1)], 3)
#     # u = round([2 * (h[i] + h[i - 1]) for i in range(1, len(h))], 3)
#     w = round([(1 / h[i]) * (a[i + 1] - a[i]) for i in range(len(a) - 1)], 3)
#     for i in range(1, len(w)):
#         v[i] = round(3 * (w[i] - w[i - 1]), 10)
#     table = zeros((len(x), len(x)))
#     table[0][0], table[len(x) - 1][len(x) - 1] = 1, 1
#     for i in range(1, len(x) - 1):
#         table[i][i - 1] = h[i - 1]
#         table[i][i] = 2 * (h[i - 1] + h[i])
#         table[i][i + 1] = h[i]
#
#     c = round(linalg.inv(table).dot(v.reshape(len(x), 1)), 3).flatten()
#     b = round([(1 / h[i]) * (a[i + 1] - a[i]) - (h[i] / 3) * (c[i + 1] + 2 * c[i]) for i in range(len(x) - 1)], 3)
#     d = round([(c[i + 1] - c[i]) / (3 * h[i]) for i in range(len(x) - 1)], 3)
#
#     return a[:len(b)], b, c[:len(b)], d


# The function is for difference cases
def cubic_spline(x, y, cases):
    """Interpolation using cubic splines.
    a_i = (s_{i+1} - s_i) / 6 * h_i
    b_i = s_i / 2
    c_i = (y_{i+1} - y_i) / h_i - (2 * h_i * s_i + h_i * s_{i+1}) / 6
    d_i = y_i
    h_i = x_{i+1} - x_i
    """

    x, y = array(x), array(y)
    s = zeros(x.shape)
    h = round([x[i + 1] - x[i] for i in range(len(x) - 1)], 8)
    table = zeros((len(x), len(x)))
    table[0][0], table[len(x) - 1][len(x) - 1] = 1, 1
    for i in range(1, len(x) - 1):
        table[i][i - 1] = h[i - 1]
        table[i][i] = 2 * (h[i - 1] + h[i])
        table[i][i + 1] = h[i]

    result = round([6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1]) for i in range(1, len(y) - 1)], 8)
    # print(result)

    table = table[1:-1, 1:-1]
    hei, wei = table.shape
    if cases == 'case1':
        s[1:-1] = round(linalg.inv(table).dot(result.reshape(len(y) - 2, 1)), 8).flatten()
    elif cases == 'case2':
        table[0][0], table[hei - 1][wei - 1] = 3 * h[0] + 2 * h[1], 2 * h[len(x) - 3] + 3 * h[len(x) - 2]
        s[1:-1] = round(linalg.inv(table).dot(result.reshape(len(y) - 2, 1)), 8).flatten()
        s[0], s[len(s) - 1] = s[1], s[len(s) - 2]
    else:
        table[0][0], table[0][1] = ((h[0] + h[1]) * (h[0] + 2 * h[1])) / h[1], (h[1] ** 2 - h[0] ** 2) / h[1]
        table[hei - 1][wei - 2] = (h[len(x) - 3] ** 2 - h[len(x) - 2] ** 2) / h[len(x) - 3]
        table[hei - 1][wei - 1] = ((h[len(x) - 2] + h[len(x) - 3]) * (h[len(x) - 2] + 2 * h[len(x) - 3])) / h[
            len(x) - 3]
        s[1:-1] = round(linalg.inv(table).dot(result.reshape(len(y) - 2, 1)), 8).flatten()
        s[0] = ((h[0] + h[1]) * s[1] - h[0] * s[2]) / h[1]
        n = len(s) - 1
        s[n] = ((h[n - 2] + h[n - 1]) * s[n - 1] - h[n - 1] * s[n - 2]) / h[n - 2]
    a = round([(s[i + 1] - s[i]) / (6 * h[i]) for i in range(len(s) - 1)], 8)
    b = s / 2
    c = round([(y[i + 1] - y[i]) / h[i] - (2 * h[i] * s[i] + h[i] * s[i + 1]) / 6 for i in range(len(y) - 1)], 8)
    d = y

    return a, b[:len(a)], c, d[:len(a)]
