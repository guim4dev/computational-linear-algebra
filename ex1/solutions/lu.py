from ex1.solutions.solution import Solution
from utils.matrix import calc_determinant
import copy

class LUSolution(Solution):
  def solve(self):
    number_of_rows = len(self.A)
    number_of_columns = len(self.A[0])

    if(number_of_rows != number_of_columns):
      return "Error"

    result = copy.deepcopy(self.A)

    for k in range(number_of_rows):
      for i in range(k+1, number_of_rows):
        result[i][k] = float(result[i][k]/result[k][k])

      for j in range(k+1, number_of_columns):
        for i in range(k+1, number_of_columns):
          result[i][j] = float(result[i][j]-result[i][k]*result[k][j])

    if self.calc_determinant:
      determinant = calc_determinant(result)
      print('Determinante:', determinant)

    print(result.view())
