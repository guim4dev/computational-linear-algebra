from src.utils.reader import getMatrixA, getVectorB
from src.ex1.solutions.cholesky import CholeskySolution
from src.ex1.solutions.gauss_seidel import GaussSeidelSolution
from src.ex1.solutions.jacobi import JacobiSolution
from src.ex1.solutions.lu import LUSolution
from src.ex1.solutions.solution import IterativeSolution

icod_map = {
  1: LUSolution,
  2: CholeskySolution,
  3: JacobiSolution,
  4: GaussSeidelSolution
}

def run():
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

  output_file_path = input('Arquivo de saída: ')
  
  print(f"A: {matrix_A}")
  print(f"B: {vector_B}")

  solution = Solution(
    A=matrix_A,
    B=vector_B,
    order=order,
    calc_determinant=idet>0,
    max_tolerance=max_tolerance).solve()
  print(solution)

  with open(output_file_path, 'w') as output_file:
    output_file.write(f"Vetor Solução: {solution['vector']}\n")
    output_file.write(f"Determinante: {solution['determinant']}\n")
  
  print("Arquivo de saída gerado com sucesso!")
