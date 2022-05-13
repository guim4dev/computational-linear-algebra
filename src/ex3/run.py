from ex3.solutions.interpolation import Interpolation
from ex3.solutions.regression import Regression

icod_map = {
  1: Interpolation,
  2: Regression,
}

def run():
  icod = int(input('ICOD: '))
  n = int(input('Número de pontos: '))
  list_of_points = []
  for i in range(n):
    x, y = map(float, input("Par de pontos X e Y: ").split())
    list.append(x,y)

  Solution = icod_map[icod]

  solution = Solution(
    list_of_points=list_of_points).solve()
  
  print(solution)

  output_file_path = input('Arquivo de saída: ')

  with open(output_file_path, 'w') as output_file:
    output_file.write(f"Autovetor: {solution['vector']}\n")
  print("Arquivo de saída gerado com sucesso!")