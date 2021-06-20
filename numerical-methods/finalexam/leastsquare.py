from numpy import polyfit, round, set_printoptions, poly1d, RankWarning
# from numpy import zeros, asarray, flipud, linalg, set_printoptions, round, poly1d
from warnings import simplefilter

# def polyfit(x, y, deg):
#     n = len(x)
#     order = int(deg) + 1
#     table = zeros((order, order))
#     table[0][0] = n
#     for i in range(order):
#         for j in range(order):
#             if i == 0 and j == 0:
#                 continue
#             table[i][j] = sum([x_i ** (i + j) for x_i in x])
#
#     b = zeros(order)
#     for i in range(order):
#         b[i] = sum([e ** i * y[j] for j, e in enumerate(x)])
#
#     table, b = asarray(table), asarray(b).reshape(order, 1)
#     coeffi = flipud(round(linalg.inv(table).dot(b), 8).flatten())
#     print(table)
#     print(b)
#
#     return coeffi


set_printoptions(precision=5, suppress=True)


def open_file():

    x_list, y_list = [], []
    file = open('./LeastSquare.txt', 'r')
    txt = file.readlines()
    for t in range(len(txt)):
        if t == 0:
            continue
        _x, _y = txt[t].split(' ')
        x_list.append(float(_x)), y_list.append(float(_y))

    return x_list, y_list


def approach_func(z_list, x, y):

    approach_list = []
    for z in z_list:
        err = []
        for i in range(len(x)):
            err.append((poly1d(z)(x[i]) - y[i]) ** 2)
        approach_list.append((sum(err) / (len(x) - (len(z) - 1))) ** 0.5)
    print("min sigma:")
    print(approach_list[approach_list.index(min(approach_list))])

    return approach_list.index(min(approach_list))


def least_square(x, y):
    print("Total inputs:", len(x))
    # find degree 12
    z = round(polyfit(x, y, 12), 5)
    print("In degree 12:")
    print(z, len(z))
    print(poly1d(z))
    z_list = []
    for i in range(len(x)):
        # skip warning
        simplefilter('ignore', RankWarning)
        z = round(polyfit(x, y, i), 5)
        # print(z)
        z_list.append(z)

    # find best
    min_coe = approach_func(z_list, x, y)
    print("Best choice:")
    print(z_list[min_coe])
    print(poly1d(z_list[min_coe]))


if __name__ == '__main__':
    x, y = open_file()
    print(x)
    print(y)
    least_square(x, y)
