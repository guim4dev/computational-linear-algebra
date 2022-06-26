from src.ex5.solutions.root import Root
from src.ex5.solutions.integral import Integral
from src.ex5.solutions.derivative import Derivative
from src.ex5.solutions.richard_extrapolation_derivative import RichardExtrapolationDerivative

icod_map = {
  1: Root,
  2: Integral,
  3: Derivative,
  4: RichardExtrapolationDerivative
}

def run():
  print('Primeiramente, precisamos que você forneça os parâmetros da função (c1, c2, c3 e c4).')
  c1 = float(input('c1: '))
  c2 = float(input('c2: '))
  c3 = float(input('c3: '))
  c4 = float(input('c4: '))

  running = True
  while(running):
    print('\nPor favor, escolha o ICOD referente à operação que deseja utilizar.')
    print('1: Encontrar a raíz da função \n2: Integrar a função \n3: Calcular a derivada em um ponto \n4: Calcular a derivada em um ponto usando a regra de extrapolação de Richard')
    icod = int(input('ICOD: '))
    Solution = icod_map[icod]

    output_file_path = input('Arquivo de saída: ')
    solution = Solution(c1=c1, c2=c2, c3=c3, c4=c4).solve()
    print(solution)

    with open(output_file_path, 'w') as output_file:
      output_file.write(f"Solução: {solution}")
    print("Arquivo de saída gerado com sucesso!")
    keep_running = int(input("Deseja realizar outra operação nesta mesma função? 1 para sim, 0 para não: "))
    if keep_running != 1:
      running = False
