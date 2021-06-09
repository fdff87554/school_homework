from numpy import zeros, round, array, math, flipud, linalg


def create_table(fx):
    height, weight = len(fx), len(fx)
    table = zeros((height, weight))

    # set f_i line
    for h in range(height):
        table[h][0] = round(fx[h], 10)

    # calculating the forward difference table
    for w in range(1, weight):
        for h in range(height - w):
            table[h][w] = round(table[h + 1][w - 1] - table[h][w - 1], 10)

    table = array(table)

    return table


def sk(s, k, direction):
    tmp = s
    for i in range(1, k):
        if direction:
            tmp = round(tmp * (s - i), 10)
        else:
            tmp = round(tmp * (s + i), 10)

    return tmp


def newton_forward(x, table, target):
    s = round((target - x[0]) / (x[1] - x[0]), 10)
    p = table[0][0]
    for i in range(1, len(x)):
        p = round(p + (sk(s, i, True) * table[0][i] / math.factorial(i)), 10)

    return p


def newton_backward(x, table, target):
    s = round((target - x[len(x) - 1]) / (x[1] - x[0]), 10)
    p = table[len(x) - 1][0]
    for i in range(1, len(x)):
        p = round(p + (sk(s, i, False) * table[len(x) - 1 - i][i] / math.factorial(i)), 10)

    return p


def start_pick(x, target):
    place = int(len(x) / 2)
    if len(x) % 2 != 0 and target < x[place]:
        place -= 1

    return place


def pk(p, k, direction):
    tmp = p
    for i in range(1, k):
        if direction:
            if (i + 1) % 2 == 0:
                tmp = round(tmp * (p - ((i + 1) // 2)), 10)
            else:
                tmp = round(tmp * (p + ((i + 1) // 2)), 10)
        else:
            if (i + 1) % 2 == 0:
                tmp = round(tmp * (p + ((i + 1) // 2)), 10)
            else:
                tmp = round(tmp * (p - ((i + 1) // 2)), 10)

    return tmp


def gauss_forward(x, table, target):
    start = start_pick(x, target)
    p = round((target - x[start]) / (x[1] - x[0]), 10)
    ans = table[start][0]
    for i in range(1, len(x)):
        if table[start - (i // 2)][i] == 0:
            break
        ans = round(ans + pk(p, i, True) * table[start - (i // 2)][i] / math.factorial(i), 10)

    return ans


def gauss_backward(x, table, target):
    start = start_pick(x, target)
    p = round((target - x[start_pick(x, target)]) / (x[1] - x[0]), 10)
    ans = table[start][0]
    for i in range(1, len(x)):
        if table[start - i + (i // 2)][i] == 0:
            break
        ans = round(ans + pk(p, i, False) * table[start - i + (i // 2)][i] / math.factorial(i), 10)

    return ans


# We will not use this function but use CubicSpline in scipy.interpolate
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
    u = round([2 * (h[i] + h[i - 1]) for i in range(1, len(h))], 3)
    w = round([(1 / h[i]) * (a[i + 1] - a[i]) for i in range(len(a) - 1)], 3)
    for i in range(1, len(w)):
        v[i] = round(3 * (w[i] - w[i - 1]), 10)
    table = zeros((len(x), len(x)))
    table[0][0], table[len(x) - 1][len(x) - 1] = 1, 1
    for i in range(1, len(x) - 1):
        table[i][i - 1] = h[i - 1]
        table[i][i] = 2 * (h[i - 1] + h[i])
        table[i][i + 1] = h[i]

    c = round(linalg.inv(table).dot(v.reshape(len(x), 1)), 3).flatten()
    b = round([(1 / h[i]) * (a[i + 1] - a[i]) - (h[i] / 3) * (c[i + 1] + 2 * c[i]) for i in range(len(x) - 1)], 3)
    d = round([(c[i + 1] - c[i]) / (3 * h[i]) for i in range(len(x) - 1)], 3)

    return a, b, c, d
