from numpy import zeros, round, array, linalg, poly1d


def open_file():

    x_list, y_list = [], []
    file = open('./CubicSpline.txt', 'r')
    txt = file.readlines()
    for t in range(len(txt)):
        _x, _y = txt[t].split(' ')
        x_list.append(float(_x)), y_list.append(float(_y))

    return x_list, y_list


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


# The function is for difference cases
def cubic_spline_tables(x, y, cases):
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

    print("Table")
    print(table)
    print("S")
    print(s)
    print("B")
    print(result)
    print(h)


if __name__ == '__main__':
    # # test x, y
    # x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    # y = [2.0, 2.008, 2.064, 2.216, 2.512, 3.0]
    # a, b, c, d = cubic_spline(x, y)
    # # output S_3 coefficient
    # print(a[2], b[2], c[2], d[2])
    # cubic_spline_tables(x, y)
    x, y = open_file()

    # question 1, s_8 coefficient
    a_set, b_set, c_set, d_set = cubic_spline(x, y, 'case1')
    # print(len(a))
    # for i in range(len(a)):
    #     print(poly1d((d[i], c[i], b[i], a[i])))
    print()
    print(poly1d((a_set[7], b_set[7], c_set[7], d_set[7])))

    # question 2, tables
    print("case1")
    cubic_spline_tables(x[:6], y[:6], 'case1')
    print("case2")
    cubic_spline_tables(x[:6], y[:6], 'case2')
    print("case3")
    cubic_spline_tables(x[:6], y[:6], 'case3')
