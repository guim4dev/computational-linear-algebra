import numpy as np
from decompositions.cholesky import CholeskyDecomposition
from decompositions.gauss_seidel import GaussSeidelDecomposition
from decompositions.jacobi import JacobiDecomposition
from decompositions.lu import LUDecomposition

icod_map = {
  1: LUDecomposition,
  2: CholeskyDecomposition,
  3: JacobiDecomposition,
  4: GaussSeidelDecomposition
}

if __name__ == '__main__':
  file_path = input('Qual é o arquivo de entrada?')
  lines = []
  with open(file_path, 'r') as file:
    lines = file.readlines()

  order = lines[0]
  icod = int(lines[1])
  idet = int(lines[2]) > 0
  matrixA = np.matrix(lines[3])
  vectorB = np.fromstring(lines[4])
  maxTolerance = 0.0
  try:
    maxTolerance = float(lines[5])
  except Exception:
    print('Não foi informado a tolerância máxima.')
    pass

  icod_map[icod].solve(order, idet, matrixA, vectorB, maxTolerance)