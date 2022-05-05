import numpy as np

def multiply_matrix_vector(matrix_a, vector):
    number_of_columns_A = len(matrix_a)
    number_of_columns_vector = range(len(vector))
    result = np.array([0.0 for _ in range(number_of_columns_A)])

    for i in range(number_of_columns_A):
        sum = 0

        for j in number_of_columns_vector:
            sum += matrix_a[i][j]*vector[j]

        result[j] = sum

    return result


def multiply_matrix_scalar(matrix_a, scalar):
    n = len(matrix_a)
    result = np.array([[0.0 for _ in range(n)] for _ in range(n)])

    for j in range(n):
        for i in range(n):
            result[i][j] = matrix_a[i][j] * scalar

    return result


def multiply_matrixes(matrix_a, matrix_b):
    number_of_rows = len(matrix_a)
    result = np.array([[0.0 for _ in range(number_of_rows)]
                      for _ in range(number_of_rows)])
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result