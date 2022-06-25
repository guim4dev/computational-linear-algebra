from src.ex5.solutions.solution import Solution
from src.ex5.solutions.derivative import Derivative

class RichardExtrapolationDerivative(Solution):
  def __init__(self, c1, c2, c3, c4, **kwargs):
    super().__init__(c1, c2, c3, c4, **kwargs)
    self.first_delta_x = float(input('Primeiro delta_x: '))
    self.second_delta_x = float(input('Segundo delta_x: '))
    self.q = self.first_delta_x/self.second_delta_x
    self.p = 1
    self.point = float(input('Ponto para derivação: '))

  def get_delta_derivative(self, delta_x):
    derivative_calculator = Derivative(self.c1, self.c2, self.c3, self.c4, delta_x=delta_x, point=self.point, chosen_method=1)
    return derivative_calculator.solve()

  def solve(self):
    first_delta_derivative = self.get_delta_derivative(self.first_delta_x)
    second_delta_derivative = self.get_delta_derivative(self.second_delta_x)
    richard_solution = first_delta_derivative + (first_delta_derivative - second_delta_derivative)/(self.q**(-self.p) - 1)
    return richard_solution