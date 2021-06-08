import warnings
import numpy as np
from matplotlib import pyplot as plt


def open_file():

    x_list, y_list = [], []
    f = open('./Hw4.txt', 'r')
    txt = f.readlines()
    for t in range(len(txt)):
        if 2 > t or t > 46:
            continue
        x, _, y = txt[t].split(' ')
        x_list.append(float(x)), y_list.append(float(y))

    return x_list, y_list


def approach_func(z_list, x, y):

    approach_list = []
    for z in z_list:
        err = []
        for i in range(len(x)):
            err.append((np.poly1d(z)(x[i]) - y[i]) ** 2)
        approach_list.append((sum(err) / (len(x) - (len(z) - 1))) ** 0.5)

    return approach_list.index(min(approach_list))


def main():

    coe_list = []
    x, y = open_file()
    # find coefficients of each power from degree 15~(n-1)
    for i in range(15, len(x)):
        # skip warning
        warnings.simplefilter('ignore', np.RankWarning)
        # find polynomial coefficients is i degree
        z = np.polyfit(x, y, i)
        # print(len(z), z)
        coe_list.append(z)

    # all coefficients output
    # print(coe_list)

    for i in range(len(coe_list)):
        # plt.title(str(i))
        plt.ylim((-1, 3))
        xp = np.linspace(min(x) - 1, max(x) + 1, 1000)
        plt.plot(x, y, '.', xp, np.poly1d(coe_list[i])(xp), '-')
    plt.show()

    # find the
    min_coe = approach_func(coe_list, x, y)
    print('Best find polynomial is at degree:', 15 + min_coe)
    xp = np.linspace(min(x) - 0.1, max(x) + 0.1, 100)
    plt.title('The Best find polynomial image:' + str(min_coe + 15))
    plt.plot(x, y, '.', xp, np.poly1d(coe_list[min_coe])(xp), '-')
    plt.show()


if __name__ == '__main__':
    main()
