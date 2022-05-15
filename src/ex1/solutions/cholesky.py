from src.ex1.solutions.solution import Solution
from src.utils.matrix import forward_substitution, backward_substitution, positive_definite

class CholeskySolution(Solution):
  def decompose(self):
    L = [[0.0] * self.order for _ in range(self.order)]

    for i in range(self.order):
      for j in range(i + 1):
        if(i == j):
          summation = sum(L[i][k]**2 for k in range(i))
          L[i][i] = (self.A[i][i]-summation)**0.5
        else:
          summation = sum(L[i][k]*L[j][k] for k in range(i))
          L[i][j] = (1.0/L[j][j])*(self.A[i][j]-summation)
      
    # include transpose on the same matrix
    for i in range(self.order):
      for j in range(i + 1, self.order):
        L[i][j] = L[j][i]
    return L
  
  def calc_cholesky_determinant(self):
    det = 1
    for i in range(self.order):
      det = det*self.A[i][i]
    return det*det ## as it is cholesky, the determinant must multiply itself (we're calculating 2 dets - one for each triangle matrix)

  def solve(self):
    if not positive_definite(self.A): raise ValueError("A matriz A não é positiva definida.")

    self.A = self.decompose()
    print(f"Decomposed Cholesky: {self.A}")
    determinant = None 
    if self.calc_determinant:
      determinant = self.calc_cholesky_determinant()
      print('Determinante:', determinant)

    matrix_y = forward_substitution(self.A, self.B, True)
    return {
      'vector': backward_substitution(self.A, matrix_y),
      'determinant': determinant
    }
