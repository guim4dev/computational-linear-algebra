from src.ex3.solutions.interpolation import Interpolation
from src.ex3.solutions.regression import Regression

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
    list_of_points.append([x,y])

  xp = float(input('Coordenada X do ponto que se deseja calcular o valor de y: '))
  Solution = icod_map[icod]

  solution = Solution(
    n=n, list_of_points=list_of_points, xp=xp).solve()
  
  print(solution)

  output_file_path = input('Arquivo de saída: ')

  with open(output_file_path, 'w') as output_file:
    output_file.write(f"Valor de y: {solution}\n")
  print("Arquivo de saída gerado com sucesso!")