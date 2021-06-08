from sympy import *

def func1(x):
    return  - 4*x**2 - 3*x + 3.8


x = symbols('x')
func_diff = diff(func1(x), x)
print(func_diff)