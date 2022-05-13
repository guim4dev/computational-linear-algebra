from src.ex1.solutions.solution import Solution
from src.utils.matrix import calc_determinant, forward_substitution, backward_substitution, positive_definite, transpose_matrix

class CholeskySolution(Solution):
  def decompose(self):
    L = [[0.0] * self.order for i in range(self.order)]

    for i in range(self.order):
      for j in range(i + 1):
        if(i == j):
          summation = sum(L[i][k]**2 for k in range(i))
          L[i][i] = (self.A[i][i]-summation)**0.5
        else:
          summation = sum(L[i][k]*L[j][k] for k in range(i))
          L[i][j] = (1.0/L[j][j])*(self.A[i][j]-summation)
      
    return L

  def solve(self):
    if not positive_definite(self.A): raise ValueError("A matriz A não é positiva definida.")

    determinant = None
    if self.calc_determinant:
      determinant = calc_determinant(self.A)
      print('Determinante:', determinant)

    cholesky_matrix_L = self.decompose()
    cholesky_matrix_U = transpose_matrix(cholesky_matrix_L) 
    matrix_y = forward_substitution(cholesky_matrix_L, self.B, True)
    return {
      'vector': backward_substitution(cholesky_matrix_U, matrix_y),
      'determinant': determinant
    }
