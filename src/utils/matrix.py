import numpy as np
import copy
import math

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


def get_auxiliar_matrix(matrix, index):
    secondary = copy.deepcopy(matrix)

    for row in range(len(secondary)):
        secondary[row] = secondary[row][1:]

    return secondary[:index] + secondary[index+1:]


def inverse_auxiliar_function(matrix, i, j):
    return np.array([row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])])


def transpose_matrix(matrix):
    result = np.array([[0.0]*len(matrix) for _ in range(len(matrix[0]))])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]

    return result


def inverse_matrix(matrix):
    cofactors = np.array()
    determinant = calc_determinant(matrix)
    if(determinant == 0):
        return 0

    for r in range(len(matrix)):
        cofactorRow = np.array()

        for c in range(len(matrix)):
            minor = inverse_auxiliar_function(matrix, r, c)
            cofactorRow.append(((-1)**(r+c)) * calc_determinant(minor))

        cofactors.append(cofactorRow)

    cofactors = transpose_matrix(cofactors)

    for r in range(len(cofactors)):
        for c in range(len(cofactors)):

            cofactors[r][c] = cofactors[r][c]/determinant

    return cofactors


def forward_substitution(matrix_l, matrix_b, control=False):
    number_of_rows = len(matrix_l)
    matrix_y = [0 for i in range(number_of_rows)]
    matrix_y[0] = matrix_b[0]
    if(control): matrix_y[0] = matrix_y[0]/matrix_l[0][0]

    for i in range(1, number_of_rows):
        summation = matrix_b[i]
        for j in range(i):
            summation -= matrix_l[i][j]*matrix_y[j]

        if(not control):
            matrix_y[i] = summation
        else:
            matrix_y[i] = summation/matrix_l[i][i]

    return matrix_y

def calc_determinant(matrix):
    number_of_rows = len(matrix)
    result = 0

    if(number_of_rows == 1):
        return matrix[0][0]

    for i in range(number_of_rows):
        result += matrix[i][0]*((-1)**i) * \
            calc_determinant(get_auxiliar_matrix(matrix, i))

    return result
