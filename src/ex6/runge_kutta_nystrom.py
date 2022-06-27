import numpy as np

class RungeKuttaNystrom:
  def __init__(self, m, c, k, a1, a2, a3, w1, w2, w3, total_time, step):
    self.m = m
    self.c = c
    self.k = k
    self.a1 = a1
    self.a2 = a2
    self.a3 = a3
    self.w1 = w1
    self.w2 = w2
    self.w3 = w3
    self.total_time = total_time
    self.step = step
    self.number_of_steps = int(total_time / step)
  
  def F(self, t):
    t_as_radians = t * np.pi / 180
    return self.a1*np.sin(self.w1*t_as_radians) + self.a2*np.sin(self.w2*t_as_radians) + self.a3*np.cos(self.w3*t_as_radians)
  
  def F_derivative(self, t, x, dx):
    return (self.F(t) - self.c*dx - self.k*x)/self.m

  def solve(self):
    dy = y = t = 0
    half_step = self.step / 2
    # t = tempo, y = deslocamento, dy = velocidade, dyy = aceleração
    t0_moment = {'tempo': t, 'deslocamento': y, 'velocidade': dy, 'aceleracao': self.F_derivative(t, y, dy)} 
    moments = [t0_moment]
    for _ in range(self.number_of_steps):
      K1 = half_step * self.F_derivative(t, y, dy)
      Q = half_step * (dy+1/2*K1)
      K2 = half_step * self.F_derivative(t+half_step, y+Q, dy+K1)
      K3 = half_step * self.F_derivative(t+half_step, y+Q, dy+K2)
      L = self.step*(dy+K3)
      K4 = half_step * self.F_derivative(t+self.step, y+L, dy+2*K3)

      # now increment Y, Y' and T
      y += self.step*(dy+(1/3)*(K1+K2+K3))
      dy += 1/3*(K1+2*K2+2*K3+K4)
      t += self.step
      moments.append({'tempo': t, 'deslocamento': y, 'velocidade': dy, 'aceleracao': self.F_derivative(t, y, dy)})

    return moments 



