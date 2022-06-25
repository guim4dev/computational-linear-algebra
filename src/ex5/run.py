from src.ex5.solutions.root import Root
from src.ex5.solutions.integral import Integral
from src.ex5.solutions.derivative import Derivative

icod_map = {
  1: Root,
  2: Integral
}

def run():
  icod = int(input('ICOD: '))
  Solution = icod_map[icod]

  c1 = float(input('c1: '))
  c2 = float(input('c2: '))
  c3 = float(input('c3: '))
  c4 = float(input('c4: '))
  output_file_path = input('Arquivo de saída: ')
  solution = Solution(c1=c1, c2=c2, c3=c3, c4=c4,).solve()
  print(solution)

  with open(output_file_path, 'w') as output_file:
    output_file.write(f"Solução: {solution}")
  print("Arquivo de saída gerado com sucesso!")
