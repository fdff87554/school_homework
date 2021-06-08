import numpy as np
import pandas as pd
from scipy.integrate import quad


def normal_probability_density(x):
    constants = 1.0 / np.sqrt(2 * np.pi)

    return constants * np.exp(((-x ** 2) / 2.0))


def main():
    # create table rows and columns
    standard_normal_table = pd.DataFrame(data=[],
                                         index=np.round(np.arange(0, 5, 0.01), 4),
                                         columns=np.round(np.arange(0.00, 0.01, 0.001), 4))

    for index in standard_normal_table.index:
        for column in standard_normal_table.columns:
            z = np.round(index + column, 4)
            value, _ = quad(normal_probability_density, np.NINF, z)
            standard_normal_table.loc[index, column] = np.round(value, 4)

    standard_normal_table.index = standard_normal_table.index.astype(str)
    standard_normal_table.columns = [str(column).ljust(4, '0') for column in standard_normal_table.columns]
    print(standard_normal_table)
    standard_normal_table.to_csv('table.csv')


if __name__ == '__main__':
    main()
