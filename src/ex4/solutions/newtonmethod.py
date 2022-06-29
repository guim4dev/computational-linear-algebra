from src.ex4.solutions.solution import Solution
from src.utils.matrix import inverse_matrix, multiply_matrix_vector, norm_vector, subtract_vector

class NewtonMethod(Solution):
    def solve(self):
        MAX_ITER = 100000
        X = [1,0,0]
        for k in range(MAX_ITER):
            J = self.Jacobian(X)
            Y = self.F(X)
            dx = multiply_matrix_vector(inverse_matrix(J), Y)
            X = subtract_vector(X, dx)
            if (norm_vector(dx) / norm_vector(X)) < self.maxTolerance:
                return X
        return 'Solução não convergiu para o número de iterações'