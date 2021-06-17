from numpy import polyfit, round, set_printoptions, poly1d, RankWarning
from warnings import simplefilter


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

    return approach_list.index(min(approach_list))


def least_square(x, y):
    print("Total inputs:", len(x))
    # find degree 12
    z = round(polyfit(x, y, 12), 5)
    print("In degree 12:")
    # print(z, len(z))
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
    least_square(x, y)
