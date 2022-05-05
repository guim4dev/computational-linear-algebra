import sys 
sys.path.append('..')
from utils.reader import getMatrixA, getVectorB
from solutions.cholesky import CholeskySolution
from solutions.gauss_seidel import GaussSeidelSolution
from solutions.jacobi import JacobiSolution
from solutions.lu import LUSolution
from ex1.solutions.solution import IterativeSolution


icod_map = {
  1: LUSolution,
  2: CholeskySolution,
  3: JacobiSolution,
  4: GaussSeidelSolution
}

if __name__ == '__main__':
  order = int(input('Ordem do sistema de equações: ')) 
  matrix_A_file_path = input('Arquivo de entrada da matriz A: ')
  matrix_A = getMatrixA(matrix_A_file_path)
  vector_B_file_path = input('Arquivo de entrada do vetor B: ')
  icod = int(input('ICOD: '))
  vector_B = getVectorB(vector_B_file_path)
  idet = int(input('IDET: '))
  Solution = icod_map[icod]
  max_tolerance = None
  if type(Solution) == IterativeSolution:
    max_tolerance = float(input('Valor de tolerância máxima:'))

  new_A = Solution.solve(order, idet, matrix_A, vector_B, max_tolerance)
