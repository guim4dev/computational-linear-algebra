from decompositions.cholesky import CholeskyDecomposition
from decompositions.gauss_seidel import GaussSeidelDecomposition
from decompositions.jacobi import JacobiDecomposition
from decompositions.lu import LUDecomposition
from decompositions.decomposition import IterativeDecomposition

import sys 
sys.path.append('..')
from utils.reader import getMatrixA, getVectorB

icod_map = {
  1: LUDecomposition,
  2: CholeskyDecomposition,
  3: JacobiDecomposition,
  4: GaussSeidelDecomposition
}

if __name__ == '__main__':
  order = int(input('Qual a ordem do sistema de equações?')) 
  matrix_A_file_path = input('Qual é o arquivo de entrada da matriz A?')
  matrix_A = getMatrixA(matrix_A_file_path)
  vector_B_file_path = input('Qual é o arquivo de entrada do vetor B?')
  icod = int(input('Informe o ICOD:'))
  vector_B = getVectorB(vector_B_file_path)
  idet = int(input('Informe o IDET:'))
  decomposition = icod_map[icod]
  max_tolerance = None
  if type(decomposition) == IterativeDecomposition:
    max_tolerance = float(input('Informe o valor de tolerância máxima:'))


  decomposition.solve(order, idet, matrix_A, vector_B, max_tolerance)
