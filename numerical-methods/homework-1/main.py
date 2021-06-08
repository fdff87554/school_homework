from methods import *
from func import *


def run(func, func_fix, a, b):
    m = bisection_method(func, a, b)
    print("Answer of Bisection Method: ", m)
    print("----------------------------------------------------------------------")
    m = false_position_method(func, a, b)
    print("Answer of False position Method: ", m)
    print("----------------------------------------------------------------------")
    m = modify_false_position_method(func, a, b)
    print("Answer of Modify false position Method: ", m)
    print("----------------------------------------------------------------------")
    m = secant_method(func, a, b)
    print("Answer of Secant Method: ", m)
    print("----------------------------------------------------------------------")
    m = newton_method(func, a)
    print("Answer of Newton Method: ", m)
    print("----------------------------------------------------------------------")
    m = fixed_point_method(func_fix, a)
    print("Answer of Fixed point Method: ", m)
    print("----------------------------------------------------------------------")


if __name__ == "__main__":

    # function one
    run(func1, func1_fix, -5, 5)
    # run(func2, func2_fix, -5, 5)
    # run(func3, func3_fix, -5, 5)
    # run(func4, func4_fix, -5, 5)
