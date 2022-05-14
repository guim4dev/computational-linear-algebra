from src.ex1.solutions.solution import IterativeSolution
from src.utils.matrix import diagonal_dominant
import copy
class JacobiSolution(IterativeSolution):
  def solve(self):
    if (not diagonal_dominant(self.A)):
      raise ValueError("A matriz A não converge.")

    solution = [1 for _ in range(self.order)]
    previous_solution = copy.deepcopy(solution)
    residues = [1]
    # residue starts at 1
    residue = 1
    steps = 0

    while (residue > self.maxTolerance):
      previous_solution = copy.deepcopy(solution)
      numerator = 0
      denominator = 0
      for i in range(self.order):
        solution[i] = self.B[i]

        for k in range(self.order):
          if (i != k):
            solution[i] += (-1)*(self.A[i][k] * previous_solution[k])

        solution[i] /= self.A[i][i]

      for i in range(self.order):
        numerator += (solution[i]-previous_solution[i])**2
        denominator += solution[i]**2

      residue = float(numerator**0.5)/(denominator**0.5)
      residues.append(residue)
      steps += 1
      print(f"Fineshed iteration {steps}...")

    return {
      'vector': solution,
      'residues': residues,
      'numberOfIterations': steps
    }
