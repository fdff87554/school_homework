import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, linspace, polyfit, poly1d
from scipy.interpolate import CubicSpline

from utils.interpolation import create_table, newton_forward, newton_backward, gauss_forward, gauss_backward, \
    cubic_spline
from utils.integration import trapezoid_rule, simpson_13_rule, simpson_38_rule
# from utils.polynomial import polyfit


def cubic_spline_test():
    x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    y = [2.0, 2.008, 2.064, 2.216, 2.512, 3.0]

    # print(cubic_spline(x, y))
    f = CubicSpline(x, y, bc_type='natural')
    xp = linspace(min(x) - 0.1, max(x) + 0.1, 100)
    plt.plot(x, y, '.', xp, f(xp), '-')
    plt.show()


def polynomial_test():
    x = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    y = [0.0, 0.20, 0.27, 0.30, 0.32, 0.33]

    # print(polyfit(x, y, 3))
    xp = linspace(min(x) - 0.1, max(x) + 0.1, 100)
    f = poly1d(polyfit(x, y, 3))
    plt.plot(x, y, '.', xp, f(xp), '-')
    plt.show()


def func(x):

    return (x ** 2) * exp(x)


def integration_test():
    print(trapezoid_rule(func, 0, 4))
    print(simpson_13_rule(func, 0, 4, 2))
    print(simpson_38_rule(func, 0, 4, 3))
    print()


def interpolation_test():
    x = [0, 1, 2, 3, 4, 5]
    fx = [1, 2, 4, 8, 16, 32]

    table = create_table(fx)
    print(newton_forward(x, table, 4.12))
    print(newton_backward(x, table, 4.12))
    print(gauss_forward(x, table, 4.12))
    print(gauss_backward(x, table, 4.12))
    print()


if __name__ == '__main__':
    # interpolation_test()
    # integration_test()
    # polynomial_test()
    cubic_spline_test()
