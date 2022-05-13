class Solution:
  can_calc_determinant = True

  def __init__(self, A, order, calc_determinant, maxTolerance):
    self.A = A
    self.order = order
    self.calc_determinant = calc_determinant
    self.maxTolerance = maxTolerance
    if self.calc_determinant and not self.can_calc_determinant:
      print('WARNING: Essa decomposição não permite o cálculo da determinante.')

  def solve(self):
    raise RuntimeError('Not implemented')