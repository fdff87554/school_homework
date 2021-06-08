from numpy import zeros, round, linalg, flipud, asarray


# We will not use the function here, and will use np.polyfit
def polyfit(x, y, deg):
    n = len(x)
    order = int(deg) + 1
    table = zeros((order, order))
    table[0][0] = n
    for i in range(order):
        for j in range(order):
            if i == 0 and j == 0:
                continue
            table[i][j] = round(sum([x_i ** (i + j) for x_i in x]), 8)

    b = zeros(order)
    for i in range(order):
        b[i] = round(sum([e ** i * y[j] for j, e in enumerate(x)]), 8)

    table, b = asarray(table), asarray(b).reshape(order, 1)
    coeffi = flipud(round(linalg.inv(table).dot(b), 8).flatten())

    return coeffi
