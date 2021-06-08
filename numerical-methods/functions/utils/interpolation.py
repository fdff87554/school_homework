from numpy import zeros, round, array, math


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
