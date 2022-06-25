from src.ex5.solutions.solution import Solution
from src.ex5.utils.polynomial_quadrature import get_polynomial_quadrature
from src.ex5.utils.gauss_quadrature import get_gauss_legendre_quadrature

class Integral(Solution):
  def __init__(self, c1, c2, c3, c4, **kwargs):
    super().__init__(c1, c2, c3, c4, **kwargs)
    self.a = float(input('a: '))
    self.b = float(input('b: '))
    self.chosen_method = int(input('Escolha um método - 1 para Gauss-Legendre; 2 para Quadratura Polinomial: '))
    if self.chosen_method not in [1, 2]:
      raise RuntimeError('Método inválido.')
    
    self.number_of_integration_points = int(input('Número de pontos de integração (entre 2 e 10): '))
    if self.number_of_integration_points < 2 or self.number_of_integration_points > 10: raise RuntimeError('Número de pontos de integração inválido.') 

  def gauss_legendre(self):
    quadrature = get_gauss_legendre_quadrature(self.number_of_integration_points)
    L = self.b - self.a
    points = map(lambda point: 0.5*(self.a + self.b + point*L), quadrature.get('points'))
    sum_pw = sum([self.F(point) * weight for point, weight in zip(points, quadrature['weights'])])
    return (L/2)*sum_pw

  def polynomial_quadrature(self):
    points, weights = get_polynomial_quadrature(self.number_of_integration_points, self.a, self.b)
    return sum([self.F(point) * weight for point, weight in zip(points, weights)]) 

  def solve(self):
    integral = { 1: self.gauss_legendre, 2: self.polynomial_quadrature }[self.chosen_method]()
    return integral