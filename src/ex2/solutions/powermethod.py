from src.ex2.solutions.solution import Solution
from src.utils.matrix import multiply_matrix_vector

class PowerMethod(Solution):
    can_calc_determinant = False
    def solve(self):
        X = [1] * self.order

        old_value = 1
        print(self.A)
        print(X)
        Y = multiply_matrix_vector(self.A, X)
        print(Y)
        value = Y[0]
        for i in range(self.order):
            Y[i] = Y[i]/value

        X = Y
        r = abs(value-old_value) / abs(value)
        while (r > self.maxTolerance):
            old_value = value
            Y = multiply_matrix_vector(self.A, X)
            value = Y[0]

            for i in range(self.order):
                Y[i] /= value

            X = Y
            r = abs(value-old_value) / abs(value)
                
        return {
        'vector': X,
        'eigenvalue': value,
    }
