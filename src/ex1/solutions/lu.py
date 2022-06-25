from src.ex1.solutions.solution import Solution
from src.utils.matrix import forward_substitution, backward_substitution

class LUSolution(Solution):
  def decompose(self):
    for k in range(self.order):
      # parte L da matriz
      for i in range(k+1, self.order):
        self.A[i][k] = float(self.A[i][k]/self.A[k][k])

      # parte U da matriz
      for j in range(k+1, self.order):
        for i in range(k+1, self.order):
          self.A[i][j] = float(self.A[i][j]-self.A[i][k]*self.A[k][j])
    return self.A

  def calc_lu_determinant(self):
    det = 1
    for i in range(self.order):
      det = det*self.A[i][i]
    return det

  def solve(self):
    self.decompose()
    determinant = None
    if self.calc_determinant:
      determinant = self.calc_lu_determinant()
      print('Determinante:', determinant)

    matrix_y = forward_substitution(self.A, self.B)
    return {
      'vector': backward_substitution(self.A, matrix_y),
      'determinant': determinant
    }
