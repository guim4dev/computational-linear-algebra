class Decomposition:
  can_calc_determinant = False

  def __init__(self, A, B, order, calc_determinant, **kwargs):
    self.A = A
    self.B = B
    self.order = order
    self.calc_determinant = calc_determinant
    if self.calc_determinant and not self.can_calc_determinant:
      print('WARNING: Essa decomposição não permite o cálculo da determinante.')

  def solve(self):
    raise RuntimeError('Not implemented')

class IterativeDecomposition(Decomposition):
   def __init__(self, A, B, order, calc_determinant, maxTolerance):
    self.maxTolerance = maxTolerance
    super().__init__(A, B, order, calc_determinant)