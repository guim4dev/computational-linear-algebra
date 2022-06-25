from src.ex5.solutions.solution import Solution
from src.ex5.utils.polynomial_quadrature import get_polynomial_quadrature
from src.ex5.utils.gauss_quadrature import get_gauss_legendre_quadrature

class Derivative(Solution):
  def __init__(self, c1, c2, c3, c4, **kwargs):
    super().__init__(c1, c2, c3, c4, **kwargs)
    self.delta_x = float(input('delta_x: '))
    self.point = int(input('Ponto para derivação: '))
    self.chosen_method = int(input('Escolha um método - 1 para Diferenças Finitas passo a frente; 2 para Diferenças Finitas passo atrás; 3 para Diferença Central: '))
    if self.chosen_method not in [1, 2, 3]:
      raise RuntimeError('Método inválido.')

  def forward_step(self):
    derivative = (self.F(self.point + self.delta_x) - self.F(self.point)) / self.delta_x
    return derivative

  def backward_step(self):
    derivative = (self.F(self.point) - self.F(self.point - self.delta_x)) / self.delta_x
    return derivative

  def central_difference(self):
    derivative = (self.F(self.point + self.delta_x) - self.F(self.point - self.delta_x)) / (2 * self.delta_x)
    return derivative

  def solve(self):
    derivative = { 1: self.forward_step, 2: self.backward_step, 3: self.central_difference }[self.chosen_method]()
    return derivative