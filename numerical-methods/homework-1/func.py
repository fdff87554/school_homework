from sympy import sin, cos, exp, log


# function one for teacher's question
def func1(x):
    return 4.98 * cos(x) + 3.2 * x * sin(2 * x) - 3 * x + 2.9


def func1_fix(x):
    return ((-2.9) - 4.98*cos(x))/(3.2*sin(2*x) - 3)


# function two
def func2(x):
    return exp(x) - 3*x*cos(2*x) - 8.3


def func2_fix(x):
    return log(3*x*cos(2*x)) + 8.3


# function three
def func3(x):
    return exp(x*sin(x))-x*cos(2*x)-2.8


def func3_fix(x):
    return log(x*cos(2*x)+2.8)/sin(x)


# function four
def func4(x):
    return 4*exp(x*sin(x)*cos(x))-10


def func4_fix(x):
    return log(2.5)/sin(x)*cos(x)
