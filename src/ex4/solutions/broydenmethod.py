from src.ex4.solutions.solution import Solution
from src.utils.matrix import add_matrixes, inverse_matrix, multiply_matrix_scalar, multiply_matrix_vector, multiply_matrixes, multiply_vectors, norm_vector, subtract_vector, transpose_vector

class BroydenMethod(Solution):
    def solve(self):
        MAX_ITER = 100000
        X = [1, 0, 0]
        B = self.Jacobian(X)
        for k in range(MAX_ITER):
            J = B
            Y = self.F(X)
            dx = multiply_matrix_vector(inverse_matrix(J), Y)
            print(dx)
            X = subtract_vector(X, dx)
            Y = subtract_vector(self.F(X), Y)
            if (norm_vector(dx) / norm_vector(X)) < self.maxTolerance:
                return X
            
            product1 = multiply_matrix_vector(B, dx)
            sub = subtract_vector(Y, product1)
            product2 = multiply_matrixes([sub], transpose_vector(dx))
            den = multiply_matrixes(transpose_vector(dx), [dx])
            result = multiply_matrixes(product2, inverse_matrix(den))
            B = add_matrixes(B, result)
        
        return 'Solução não convergiu para o número de iterações'