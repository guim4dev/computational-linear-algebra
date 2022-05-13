from src.ex2.solutions.powermethod import PowerMethod
from src.ex2.solutions.jacobimethod import JacobiMethod

from src.utils.reader import getMatrixA

icod_map = {
  1: PowerMethod,
  2: JacobiMethod,
}

def run():
  order = int(input('Ordem N da matriz A: '))  
  matrix_A_file_path = input('Arquivo de entrada da matriz A: ')
  matrix_A = getMatrixA(matrix_A_file_path)
  icod = int(input('ICOD: '))
  idet = int(input('IDET: '))
  max_tolerance = float(input('Valor de tolerância máxima:'))

  Solution = icod_map[icod]

  solution = Solution(
    A=matrix_A,
    order=order,
    calc_determinant=idet>0,
    max_tolerance=max_tolerance).solve()

  output_file_path = input('Arquivo de saída: ')