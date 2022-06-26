import numpy as np

class Solution:
  def __init__(self, c1, c2, c3, c4, **kwargs):
    self.c1 = c1
    self.c2 = c2
    self.c3 = c3
    self.c4 = c4

  def solve(self):
    raise RuntimeError('Not implemented')

  def F(self, X):
    return self.c1*np.exp(self.c2*X) + self.c3*X**self.c4

  def F_derivative(self, X):
    return self.c1*self.c2*np.exp(self.c2*X) + self.c3*self.c4*X**(self.c4-1)
