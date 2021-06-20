import matplotlib.pyplot as plt
from numpy import exp, linspace, polyfit, poly1d, set_printoptions
# from scipy.interpolate import CubicSpline

# from utils.polynomial import polyfit
from utils.interpolation import create_table, newton_forward, newton_backward, gauss_forward, gauss_backward
from utils.integration import trapezoid_rule, simpson_13_rule, simpson_38_rule
from utils.cubic_spline import cubic_spline


set_printoptions(precision=3, suppress=True)


def cubic_spline_test():
    x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    y = [2.0, 2.008, 2.064, 2.216, 2.512, 3.0]
    print("case1")
    print(cubic_spline(x, y, 'case1'))
    print("case2")
    print(cubic_spline(x, y, 'case2'))
    print("case3")
    print(cubic_spline(x, y, 'case3'))
    # f = CubicSpline(x, y, bc_type='natural')
    # xp = linspace(min(x) - 0.1, max(x) + 0.1, 100)
    # plt.plot(x, y, '.', xp, f(xp), '-')
    # plt.show()


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
    x = [0, 1, 2, 3, 4, 5, 6]
    fx = [1, 2, 4, 8, 16, 32, 64]
    # x = [1.0, 3.0, 5.0, 7.0, 9.0]
    # fx = [0, 1.0986, 1.6094, 1.9459, 2.1972]
    target = 4.12

    table = create_table(fx)
    print(table)
    print(newton_forward(x, table, target))
    print(newton_backward(x, table, target))
    print(gauss_forward(x, table, target))
    print(gauss_backward(x, table, target))
    print()


if __name__ == '__main__':
    interpolation_test()
    integration_test()
    polynomial_test()
    cubic_spline_test()
