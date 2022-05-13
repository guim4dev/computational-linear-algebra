class Solution:
  can_calc_determinant = True

  def __init__(self, list_of_points):
    self.list_of_points = list_of_points
    if self.calc_determinant and not self.can_calc_determinant:
      print('WARNING: Essa decomposição não permite o cálculo da determinante.')

  def solve(self):
    raise RuntimeError('Not implemented')