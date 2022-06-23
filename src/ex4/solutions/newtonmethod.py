from src.ex4.solutions.solution import Solution
from src.utils.matrix import inverse_matrix, multiply_matrix_vector, subtract_vector

class NewtonMethod(Solution):
    def solve(self):
        X = [1,1,1]
        for k in range(self.maxIter):
            J = self.Jacobian(X)
            Y = self.F(X)
            dx = multiply_matrix_vector(inverse_matrix(J), Y)
            X = subtract_vector(X, dx)
            print(X)
