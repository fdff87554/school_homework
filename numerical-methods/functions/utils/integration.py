# This file is for integral function of Trapezoid Rule, Simpson 1/3 Rule, Simpson 3/8 Rule
from numpy import round, linspace, sum


def trapezoid_rule(f, a, b, n=50):
    """Approximate the integral of f(x) from a to b by the trapezoid rule.

    The trapezoid rule approximates the integral Tn = h/2 * \sum_{i=1}^{n-1} (f(x_i) + f(x_{i-1})
    h = (b - a)/n, x_i = a + ih

    :parameter:
    f:      function
            Vectorized function of a single variable
    a, b:   numbers
            Interval of integration [a, b]
    n:      integer
            Number of subintervals of [a, b]

    :return:
    float
            Approximation of the integral of f(x) from a to b using
            the trapezoid rule with n subintervals of equal length.
    """
    x = linspace(a, b, n+1)
    y = f(x)
    y_left, y_right = y[:-1], y[1:]
    h = (b - a) / n
    trapz = round((h / 2) * sum(y_right + y_left), 10)

    return trapz


def simpson_13_rule(f, a, b, n=50):
    """Approximate the integral of f(x) from a to b by the simpson's 1/3 rule.

    The Simpson's 1/3 rule approximates the integral S = h/3 * (f(a) + 4f((a+b)/2) + f(b))
    If [a, b] split up into n subintervals, Sn = h/3 * \sum_{j=1}^{n/2} f(x_{2j-2})+4f(x_{xj-1})+f(x_2j)
    h = b - a / 2, x_j = a + jh

    :parameter:
    f:      function
            Vectorized function of a single variable
    a, b:   numbers
            Interval of integration [a, b]
    n:      integer
            Number of subintervals of [a, b]

    :return:
    float
            Approximation of the integral of f(x) from a to b using
            the trapezoid rule with n subintervals of equal length.
    """
    if n % 2 == 1:
        raise ValueError('n must be an even integer.')
    h = (b - a) / n
    x = linspace(a, b, n+1)
    y = f(x)
    simps = h / 3 * sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])

    return simps


def simpson_38_rule(f, a, b, n=51):
    """Approximate the integral of f(x) from a to b by the simpson's 3/8 rule.

    The Simpson's 3/8 rule approximates the integral S = h * 3/8 * (f(a) + 3f((2 * a + b)/3) + 3f((a + 2 * b)/3) + f(b))
    If [a, b] split up into n subintervals, Sn = h * 3/8 * \sum_{j=1}^{n/3} f(x_{3j-3})+3f(x_{3j-2})+3f(x_{3j-1})+f(x_{3j})
    h = b - a / 2, x_j = a + jh

    :parameter:
    f:      function
            Vectorized function of a single variable
    a, b:   numbers
            Interval of integration [a, b]
    n:      integer
            Number of subintervals of [a, b]
    :return:
    float
            Approximation of the integral of f(x) from a to b using
            the trapezoid rule with n subintervals of equal length.
    """
    if n % 2 == 0 or n < 3:
        raise ValueError('n must be an odd integer and bigger then 3.')
    h = (b - a) / n
    x = linspace(a, b, n + 1)
    y = f(x)
    simps = h * 3 / 8 * sum(y[0:-1:3] + 3 * y[1::3] + 3 * y[2::3] + y[3::3])

    return simps
