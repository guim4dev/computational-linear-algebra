from src.ex4.solutions.solution import Solution
from src.utils.matrix import norm_vector, subtract_vector
from src.ex1.solutions.lu import LUSolution
import numpy as np

class BroydenMethod(Solution):
    def solve(self):
        MAX_ITER = 100000
        X0 = np.array([1,0,0])
        B = np.array(self.Jacobian(X0))
        for _ in range(MAX_ITER):
            Y = np.array(self.F(X0))
            dX = np.array(LUSolution(B,Y, 3, False).solve()['vector'])
            X1 = X0 - dX
            Y = np.array(subtract_vector(self.F(X1), self.F(X0)))
            if norm_vector(dX)/norm_vector(X1) < self.maxTolerance:
                return X1
            else:
                Y = Y.reshape(-1,1)
                dX = dX.reshape(-1,1)
                B = B - (np.matmul((Y + np.matmul(B,dX)), dX.T)) / np.matmul(dX.T,dX)
            X0 = X1
        return "Solução não convergiu"