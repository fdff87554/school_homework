from numpy import zeros, round, array, linalg


def open_file():

    x_list, y_list = [], []
    file = open('./CubicSpline.txt', 'r')
    txt = file.readlines()
    for t in range(len(txt)):
        if t == 0:
            continue
        _x, _y = txt[t].split(' ')
        x_list.append(float(_x)), y_list.append(float(_y))

    return x_list, y_list


def cubic_spline(x, y):
    """Interpolation using natural cubic splines.

    The natural cubic spline S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i) ** 2 + d_i(x - x_i) ** 3
    a_i = f(x_i) = y_i
    b_i = (1 / h_i) * (a_{i+1} - a_i) - (h_i / 3) * (c_{i+i} + 2 * c_{i})
    d_i = (c_{i+1} - c_i) / (3 * h_i)
    v_i = h_{i-1} * c_{i-i} + u_i * c_i + h_i * c_{i+1} = 3 * (w_i - w_{i-1})
    w_i = (1/h_i) * (a_{i+1} - a_i)
    u_i = 2 * (h_{i-1} + h_i)
    h_i = x_{i+1} - x_i
    """

    x, y = array(x), array(y)
    a = y
    v = zeros(x.shape)
    h = round([x[i + 1] - x[i] for i in range(len(x) - 1)], 3)
    # u = round([2 * (h[i] + h[i - 1]) for i in range(1, len(h))], 3)
    w = round([(1 / h[i]) * (a[i + 1] - a[i]) for i in range(len(a) - 1)], 3)
    for i in range(1, len(w)):
        v[i] = round(3 * (w[i] - w[i - 1]), 10)
    table = zeros((len(x), len(x)))
    table[0][0], table[len(x) - 1][len(x) - 1] = 1, 1
    for i in range(1, len(x) - 1):
        table[i][i - 1] = h[i - 1]
        table[i][i] = 2 * (h[i - 1] + h[i])
        table[i][i + 1] = h[i]
    print(table)

    c = round(linalg.inv(table).dot(v.reshape(len(x), 1)), 3).flatten()
    b = round([(1 / h[i]) * (a[i + 1] - a[i]) - (h[i] / 3) * (c[i + 1] + 2 * c[i]) for i in range(len(x) - 1)], 3)
    d = round([(c[i + 1] - c[i]) / (3 * h[i]) for i in range(len(x) - 1)], 3)

    print(a[:len(b)], b, c[:len(b)], d)


if __name__ == '__main__':
    x, y = open_file()
    cubic_spline(x[:6], y[:6])
