from utils.interpolation import *


def main():
    # basic parameter
    # names = ['f(0.28 y)', 'f(0.53 y)', 'f(0.78 y)', 'f(1.03 y)', 'f(1.28 y)',
    #          'f(1.53 y)', 'f(1.78 y)', 'f(2.03 y)', 'f(2.28 y)', 'f(2.53 y)']
    x = [0.28, 0.53, 0.78, 1.03, 1.28, 1.53, 1.78, 2.03, 2.28, 2.53]
    y = [0.7200, 0.8400, 0.9600, 1.0800, 1.2000, 1.3200, 1.4400, 1.5600, 1.6800, 1.8000]
    f_028_y = [5.7398, 6.2854, 6.8206, 7.3455, 7.8601, 8.3646, 8.8591, 9.3437, 9.8186, 10.2839]
    f_053_y = [5.3736, 5.7908, 6.1734, 6.5223, 6.8390, 7.1248, 7.3812, 7.6098, 7.8124, 7.9909]
    f_078_y = [4.7095, 4.9192, 5.0630, 5.1458, 5.1733, 5.1515, 5.0869, 4.9862, 4.8567, 4.7058]
    f_103_y = [3.7941, 3.7417, 3.5953, 3.3692, 3.0789, 2.7410, 2.3728, 1.9919, 1.6161, 1.2635]
    f_128_y = [2.6891, 2.3513, 1.9071, 1.3879, 0.8268, 0.2579, -0.2844, -0.7666, -1.1564, -1.4236]
    f_153_y = [1.4713, 0.8623, 0.1633, -0.5682, -1.2736, -1.8954, -2.3786, -2.6730, -2.7349, -2.5280]
    f_178_y = [0.2335, -0.5907, -1.4475, -2.2448, -2.8935, -3.3109, -3.4250, -3.1776, -2.5267, -1.4490]
    f_203_y = [-0.9136, -1.8522, -2.7157, -3.3721, -3.7018, -3.6045, -3.0051, -1.8581, -0.1502, 2.0984]
    f_228_y = [-1.8397, -2.7460, -3.4136, -3.6718, -3.3801, -2.4390, -0.7973, 1.5440, 4.5319, 8.0655]
    f_253_y = [-2.3919, -3.0728, -3.2964, -2.8626, -1.6315, 0.4636, 3.4107, 7.1197, 11.4308, 16.1293]

    # count out the tables
    tables = [create_table(f_028_y), create_table(f_053_y), create_table(f_078_y),
              create_table(f_103_y), create_table(f_128_y), create_table(f_153_y),
              create_table(f_178_y), create_table(f_203_y), create_table(f_228_y),
              create_table(f_253_y)]

    # newton forward
    print('Newton forward')
    # count answer (1.0, 1.25)
    x_re = []
    for table in tables:
        x_re.append(newton_forward(y, table, 1.25))
    x_table = create_table(x_re)
    ans = newton_forward(x, x_table, 1.0)
    print(ans)
    # count answer (1.6, 1.72)
    x_re = []
    for table in tables:
        x_re.append(newton_forward(y, table, 1.72))
    x_table = create_table(x_re)
    ans = newton_forward(x, x_table, 1.6)
    print(ans)
    # count answer (2.2, 1.00)
    x_re = []
    for table in tables:
        x_re.append(newton_forward(y, table, 1.00))
    x_table = create_table(x_re)
    ans = newton_forward(x, x_table, 2.2)
    print(ans)

    # newton backward
    print('Newton backward')
    # count answer (1.0, 1.25)
    x_re = []
    for table in tables:
        x_re.append(newton_backward(y, table, 1.25))
    x_table = create_table(x_re)
    ans = newton_backward(x, x_table, 1.0)
    print(ans)
    # count answer (1.6, 1.72)
    x_re = []
    for table in tables:
        x_re.append(newton_backward(y, table, 1.72))
    x_table = create_table(x_re)
    ans = newton_backward(x, x_table, 1.6)
    print(ans)
    # count answer (2.2, 1.00)
    x_re = []
    for table in tables:
        x_re.append(newton_backward(y, table, 1.00))
    x_table = create_table(x_re)
    ans = newton_backward(x, x_table, 2.2)
    print(ans)

    # gauss forward
    print('Gauss forward')
    # count answer (1.0, 1.25)
    x_re = []
    for table in tables:
        x_re.append(gauss_forward(y, table, 1.25))
    x_table = create_table(x_re)
    ans = gauss_forward(x, x_table, 1.0)
    print(ans)
    # count answer (1.6, 1.72)
    x_re = []
    for table in tables:
        x_re.append(gauss_forward(y, table, 1.72))
    x_table = create_table(x_re)
    ans = gauss_forward(x, x_table, 1.6)
    print(ans)
    # count answer (2.2, 1.00)
    x_re = []
    for table in tables:
        x_re.append(gauss_forward(y, table, 1.00))
    x_table = create_table(x_re)
    ans = gauss_forward(x, x_table, 2.2)
    print(ans)

    # gauss backward
    print('Gauss backward')
    # count answer (1.0, 1.25)
    x_re = []
    for table in tables:
        x_re.append(gauss_backward(y, table, 1.25))
    x_table = create_table(x_re)
    ans = gauss_backward(x, x_table, 1.0)
    print(ans)
    # count answer (1.6, 1.72)
    x_re = []
    for table in tables:
        x_re.append(gauss_backward(y, table, 1.72))
    x_table = create_table(x_re)
    ans = gauss_backward(x, x_table, 1.6)
    print(ans)
    # count answer (2.2, 1.00)
    x_re = []
    for table in tables:
        x_re.append(gauss_backward(y, table, 1.00))
    x_table = create_table(x_re)
    ans = gauss_backward(x, x_table, 2.2)
    print(ans)


if __name__ == '__main__':
    main()
