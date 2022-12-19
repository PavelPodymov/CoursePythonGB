"""class Matrix"""

import numpy as np
import pandas as pd


class Matrix:
    """class Matrix"""

    def __init__(self, my_matrix):
        self.matrix = my_matrix

    def __str__(self):
        return '\n' + pd.DataFrame(self.matrix).to_string(index=False, header=False)

    def __add__(self, other):
        self.matrix = np.array(self.matrix) + np.array(other.matrix)
        return Matrix.__str__(self)


first_m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second_m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(first_m)
print(second_m)
print(first_m + second_m)
