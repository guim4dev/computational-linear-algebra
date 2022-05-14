import copy
import math

def multiply_matrix_vector(matrix_a, vector):
    number_of_rows_A = len(matrix_a)
    number_of_columns_vector = range(len(vector))
    result = [0.0 for _ in range(number_of_rows_A)]

    for i in range(number_of_rows_A):
        sum = 0
        for j in number_of_columns_vector:
            sum += matrix_a[i][j]*vector[j]
        result[i] = sum
    return result


def multiply_matrix_scalar(matrix_a, scalar):
    n = len(matrix_a)
    result = [[0.0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(n):
            result[i][j] = matrix_a[i][j] * scalar

    return result


def multiply_matrixes(matrix_a, matrix_b):
    number_of_rows = len(matrix_a)
    result = [[0.0 for _ in range(number_of_rows)] for _ in range(number_of_rows)]
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
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]


def transpose_matrix(matrix):
    result = [[0.0]*len(matrix) for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]

    return result


def inverse_matrix(matrix):
    cofactors = []
    determinant = calc_determinant(matrix)
    if(determinant == 0):
        return 0

    for r in range(len(matrix)):
        cofactorRow = []

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
    if control: matrix_y[0] = matrix_y[0]/matrix_l[0][0]

    for i in range(1, number_of_rows):
        summation = matrix_b[i]
        for j in range(i):
            summation -= matrix_l[i][j]*matrix_y[j]

        matrix_y[i] = summation
        if control: matrix_y[i] = matrix_y[i]/matrix_l[i][i]

    return matrix_y


def backward_substitution(matrix_u, matrix_y):
    number_of_rows = len(matrix_u)
    matrix_x = [0 for _ in range(number_of_rows)]

    matrix_x[number_of_rows-1] = matrix_y[number_of_rows-1] / \
        matrix_u[number_of_rows-1][number_of_rows-1]

    for i in range(number_of_rows-2, -1, -1):
        summation = matrix_y[i]
        for j in range(i+1, number_of_rows):
            summation -= matrix_u[i][j]*matrix_x[j]
        matrix_x[i] = summation/float(matrix_u[i][i])

    return matrix_x


def calc_determinant(matrix):
    number_of_rows = len(matrix)
    result = 0

    if(number_of_rows == 1):
        return matrix[0][0]

    for i in range(number_of_rows):
        result += matrix[i][0]*((-1)**i) * \
            calc_determinant(get_auxiliar_matrix(matrix, i))

    return result


def positive_definite(matrix):
    return is_simetric(matrix) and follows_sylvesters_criterion(matrix)


def is_simetric(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    if(number_of_rows != number_of_columns):
        return -1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] != matrix[j][i]):
                return False

    return True


def follows_sylvesters_criterion(matrix):
    for i in range(len(matrix)):
        secondary = get_main_minor(matrix, i)
        if(calc_determinant(secondary) <= 0):
            return False

    return True


def get_main_minor(matrix, index):
    result = [[matrix[row][column]
               for row in range(index + 1)] for column in range(index + 1)]
    return result

def get_biggest_element_not_in_diagonal(matrix):
    n = len(matrix)
    if (n != len(matrix[0])):
        raise Exception("Matriz tem que ser quadrada")
    value = -math.inf
    for i in range(n):
        for j in range(n):
            if (i!=j and abs(matrix[i][j]) > value):
                value = abs(matrix[i][j])
                index = (i,j)
    return index

def calcute_phi(matrix, index):
    den = (matrix[index[0]][index[0]] -
                   matrix[index[1]][index[1]])

    if(matrix[index[0]][index[0]] == matrix[index[1]][index[1]]):
        return math.pi/4
    else:
        return math.atan(2*matrix[index[0]][index[1]]/den)/2
 

def calculate_p_matrix(matrix, index):
    n = len(matrix)
    phi = 0

    P = [[float(i == j) for j in range(n)] for i in range(n)]
    
    phi = calcute_phi(matrix, index)

    P[index[0]][index[0]] = math.cos(phi)
    P[index[1]][index[1]] = math.cos(phi)
    P[index[0]][index[1]] = -math.sin(phi)
    P[index[1]][index[0]] = math.sin(phi)

    return P


def diagonal_dominant(matrix):
    for i in range(len(matrix)):
        lines_summation = 0
        columns_summation = 0
        for j in range(len(matrix)):
            if (i != j):
                lines_summation += math.fabs(matrix[i][j])
                columns_summation += math.fabs(matrix[j][i])

        if(matrix[i][i] < lines_summation or matrix[i][i] < columns_summation):
            return False

    return True