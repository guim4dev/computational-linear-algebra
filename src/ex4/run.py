from src.ex4.solutions.newtonmethod import NewtonMethod
from src.ex4.solutions.broydenmethod import BroydenMethod

icod_map = {
  1: NewtonMethod,
  2: BroydenMethod,
}

def run():
  icod = int(input('ICOD: '))

  t1 = float(input('t1: '))
  t2 = float(input('t2: '))
  maxTolerance = float(input('maxTolerance: '))
  maxIter = int(input('maxIter: '))

  Solution = icod_map[icod]

  solution = Solution(
    t1=t1, t2=t2, maxTolerance=maxTolerance, maxIter=maxIter).solve()
  
  print(solution)

  output_file_path = input('Arquivo de saída: ')

  with open(output_file_path, 'w') as output_file:
    output_file.write(f"Valor de y: {solution}\n")
  print("Arquivo de saída gerado com sucesso!")