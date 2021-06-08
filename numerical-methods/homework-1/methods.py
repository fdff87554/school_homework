from numpy import abs
from sympy import symbols, diff


def bisection_method(func, a, b):
    x = symbols('x')
    # r_e is for rounded of error
    r_e = 10 ** -10
    max_t = 1000
    # bisection method
    if func(x).evalf(subs={x: a}) * func(x).evalf(subs={x: b}) >= 0:
        print("Bisection method fails. The f(a)*f(b) > 0.")
        return None
    cnt = 0
    a_n = a
    b_n = b
    m = 0
    print("Bisection method - {}: Step {}: a={}, b={}, m={}".format(func.__name__, cnt, a_n, b_n, m))
    while abs(a_n - b_n) >= r_e and cnt <= max_t:
        cnt += 1
        m = (a_n + b_n) / 2
        if func(x).evalf(subs={x: a_n}) * func(x).evalf(subs={x: m}) <= 0:
            a_n = a_n
            b_n = m
        else:
            a_n = m
            b_n = b_n
        print("Bisection method - {}: Step {}: a={}, b={}, m={}".format(func.__name__, cnt, a_n, b_n, m))

    return m


def false_position_method(func, a, b):
    x = symbols('x')
    # r_e is for rounded of error
    r_e = 10 ** -10
    max_t = 1000
    # false position method
    if func(x).evalf(subs={x: a}) * func(x).evalf(subs={x: b}) >= 0:
        print("False position method fails. The f(a)*f(b) > 0.")
        return None
    cnt = 0
    a_n = a
    b_n = b
    m = a_n
    print("False position method - {}: Step {}: a={}, b={}, m={}".format(func.__name__, cnt, a_n, b_n, m))
    while abs(func(x).evalf(subs={x: m})) >= r_e and cnt <= max_t:
        cnt += 1
        m = (func(x).evalf(subs={x: b_n}) * a_n - func(x).evalf(subs={x: a_n}) * b_n) / \
            (func(x).evalf(subs={x: b_n}) - func(x).evalf(subs={x: a_n}))
        if func(x).evalf(subs={x: a_n}) * func(x).evalf(subs={x: m}) < 0:
            a_n = a_n
            b_n = m
        else:
            a_n = m
            b_n = b_n
        print("False position method - {}: Step {}: a={}, b={}, m={}".format(func.__name__, cnt, a_n, b_n, m))

    return m


def modify_false_position_method(func, a, b):
    x = symbols('x')
    # r_e is for rounded of error
    r_e = 10 ** -10
    max_t = 1000
    # false position method
    if func(x).evalf(subs={x: a}) * func(x).evalf(subs={x: b}) >= 0:
        print("Modify false position method fails. The f(a)*f(b) > 0.")
        return None
    cnt = 0
    f_a = func(x).evalf(subs={x: a})
    f_b = func(x).evalf(subs={x: b})
    m = a
    print("Modify false position method - {}: Step {}: a={}, b={}, m={}".format(func.__name__, cnt, a, b, m))
    while abs(func(x).evalf(subs={x: m})) >= r_e and cnt <= max_t:
        cnt += 1
        m = (f_b * a - f_a * b) / (f_b - f_a)
        if f_a * func(x).evalf(subs={x: m}) < 0:
            f_a = f_a / 2
            f_b = func(x).evalf(subs={x: m})
            b = m
        else:
            f_a = func(x).evalf(subs={x: m})
            f_b = f_b / 2
            a = m
        print("Modify false position method - {}: Step {}: a={}, b={}, m={}".format(func.__name__, cnt, a, b, m))

    return m


def fixed_point_method(func, a):
    x = symbols('x')
    # r_e is for rounded of error
    r_e = 10 ** -5
    max_t = 1000
    cnt = 0
    x_old = a
    x_new = func(x).evalf(subs={x: x_old})
    print("Fixed point method - {}: Step {}: old={}, new={}".format(func.__name__, cnt, x_old, x_new))
    while abs(x_new - x_old) >= r_e and cnt <= max_t:
        cnt += 1
        x_old = x_new
        x_new = func(x).evalf(subs={x: x_old})
        print("Fixed point method - {}: Step {}: old={}, new={}".format(func.__name__, cnt, x_old, x_new))

    return x_new


def secant_method(func, a, b):
    x = symbols('x')
    # r_e is for rounded of error
    r_e = 10 ** -10
    max_t = 1000
    cnt = 0
    c = 0
    print("Secant method - {}: Step {}: a={}, b={}, c={}".format(func.__name__, cnt, a, b, c))
    while abs(b - a) >= r_e and cnt <= max_t:
        cnt += 1
        c = (a * func(x).evalf(subs={x: b}) - b * func(x).evalf(subs={x: a})) / \
            (func(x).evalf(subs={x: b}) - func(x).evalf(subs={x: a}))
        a = b
        b = c
        print("Secant method - {}: Step {}: a={}, b={}, c={}".format(func.__name__, cnt, a, b, c))

    return b


def newton_method(func, s):
    # set differential function
    x = symbols('x')
    func_diff = diff(func(x), x)
    # r_e is for rounded of error
    r_e = 10 ** -10
    max_t = 1000
    cnt = 0
    delta = s
    print("Newton method - {}: Step {}: x={}, delta={}".format(func.__name__, cnt, s, delta))
    while abs(delta) >= r_e and cnt <= max_t:
        cnt += 1
        delta = func(x).evalf(subs={x: s}) / func_diff.evalf(subs={x: s})
        s = s - delta
        print("Newton method - {}: Step {}: x={}, delta={}".format(func.__name__, cnt, s, delta))

    return s
