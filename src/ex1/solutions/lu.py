from src.ex1.solutions.solution import Solution
from src.utils.matrix import calc_determinant, forward_substitution, backward_substitution, transpose_matrix
import copy

class LUSolution(Solution):
  def decompose(self):
    number_of_rows = len(self.A)
    number_of_columns = len(self.A[0])
    result = copy.deepcopy(self.A)

    for k in range(number_of_rows):
      # parte L da matriz
      for i in range(k+1, number_of_rows):
        result[i][k] = float(result[i][k]/result[k][k])

      # parte U da matriz
      for j in range(k+1, number_of_columns):
        for i in range(k+1, number_of_columns):
          result[i][j] = float(result[i][j]-result[i][k]*result[k][j])
    return result

  def solve(self):
    determinant = None
    if self.calc_determinant:
      determinant = calc_determinant(self.A) # Mudar para usar as propriedades da matriz LU
      print('Determinante:', determinant)

    lu_matrix = self.decompose()
    matrix_y = forward_substitution(lu_matrix, self.B)
    return {
      'vector': backward_substitution(lu_matrix, matrix_y),
      'determinant': determinant
    }

    
