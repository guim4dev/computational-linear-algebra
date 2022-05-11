from ex1.solutions.solution import Solution
from utils.matrix import get_transposed_matrix

class CholeskySolution(Solution):
  def decompose(self):
    n = len(self.A)
    m = len(self.A[0])

    if n != m:
      raise Exception("ERRO: Matriz não é quadrada")

    L = [[0.0] * n for i in range(n)]

    for i in range(n):
      for j in range(i+1):
        tmp = sum(L[i][k] * L[j][k] for k in range(j))

        if i == j:
          L[i][j] = (self.A[i][j] - tmp)**0.5
        else:
          L[i][j] = (1.0 / L[j][j] * (self.A[i][j] - tmp))
      
      return L

  def solve(self):
    L = self.decompose()
    LT = get_transposed_matrix(L)

    #Incomplete