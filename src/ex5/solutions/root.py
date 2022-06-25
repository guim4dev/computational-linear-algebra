from src.ex5.solutions.solution import Solution

class Root(Solution):
  def __init__(self, c1, c2, c3, c4, **kwargs):
    super().__init__(c1, c2, c3, c4, **kwargs)
    self.a = int(input('a: '))
    self.b = int(input('b: '))
    self.chosen_method = int(input('Escolha um método - 1 para Bisseção; 2 para Newton: '))
    if self.chosen_method not in [1, 2]:
      raise RuntimeError('Método inválido.')
    
    if self.chosen_method == 1: self.maxTolerance = float(input('Tolerância: '))

  def bisection(self):
    current_x = 0 
    while abs(self.a - self.b) > self.maxTolerance:
      current_x = (self.a + self.b) / 2
      if self.F(current_x) > 0:
        self.b = current_x
      else:
        self.a = current_x

    return current_x

  def newton(self):
    pass

  def solve(self):
    root = { 1: self.bisection, 2: self.newton }[self.chosen_method]()
    return root