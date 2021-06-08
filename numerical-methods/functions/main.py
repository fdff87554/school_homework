import numpy as np

from utils.interpolation import create_table, newton_forward, newton_backward, gauss_forward, gauss_backward
from utils.integration import trapezoid_rule, simpson_13_rule, simpson_38_rule


def polynomial_test():
    x = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    y = [0.0, 0.20, 0.27, 0.30, 0.32, 0.33]

    print(np.polyfit(x, y, 3))


def func(x):

    return (x ** 2) * np.exp(x)


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
    interpolation_test()
    integration_test()
    polynomial_test()
