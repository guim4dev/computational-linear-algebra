from src.ex1.run import run as ex1_run
from src.ex2.run import run as ex2_run

ex_map = {
  1: ex1_run,
  2: ex2_run
}

if __name__ == '__main__':
  ex_map[int(input('Escolha o trabalho que deseja executar: '))]()