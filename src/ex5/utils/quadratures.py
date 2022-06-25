from src.ex1.solutions.lu import LUSolution

def get_verdermonde_weights(points, a, b):
  N = len(points)
  # solve AX = B system
  # A = Vandermonde matrix
  A = []
  for i in range(N):
    current_row = []
    for j in range(N):
      current_row.append(points[j]**i)
    A.append(current_row)
  print(f"Verdermonde Matrix: \n{A}")

  B = [(b**(i+1) - a**(i+1))/(i+1) for i in range(N)]
  print(f"\nB: {B}")
  # use LU decomposition to solve the system
  solver = LUSolution(A=A, B=B, order=N, calc_determinant=False)
  weights = solver.solve().get('vector')
  return weights

def get_polynomial_quadrature(number_of_points, a, b):
  points = []
  weights = []
  L = b - a
  if number_of_points == 2:
    points = [a, b]
    weights = [L/2, L/2]
  elif number_of_points == 3:
    points = [a, (a + b) / 2, b]
    weights = [L/6, 2*L/3, L/6]
  else:
    delta = L / (number_of_points - 1)
    middle_points = [a + i*delta for i in range(1, number_of_points-1)]
    points = [a] + middle_points + [b]
    weights = get_verdermonde_weights(points, a, b)
  return points, weights
