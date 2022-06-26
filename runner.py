from src.ex1.run import run as ex1_run
from src.ex2.run import run as ex2_run
from src.ex3.run import run as ex3_run
from src.ex4.run import run as ex4_run
from src.ex5.run import run as ex5_run
from src.ex6.run import run as ex6_run

ex_map = {
  1: ex1_run,
  2: ex2_run,
  3: ex3_run,
  4: ex4_run,
  5: ex5_run,
  6: ex6_run,
}

if __name__ == '__main__':
  ex_map[int(input('Escolha o trabalho que deseja executar: '))]()