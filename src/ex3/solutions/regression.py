from src.ex3.solutions.solution import Solution
from src.utils.matrix import inverse_matrix, multiply_matrix_vector
class Regression(Solution):
    def solve(self):
        sum_n, sum_x, sum_x2, sum_y, sum_xy = 0, 0, 0, 0, 0
        for i in range(self.n):
            sum_n += 1
            sum_x += self.list_of_points[i][0]
            sum_x2 += self.list_of_points[i][0]**2
            sum_y += self.list_of_points[i][1]
            sum_xy += self.list_of_points[i][0] * self.list_of_points[i][1]

        A = []
        A.append([sum_n, sum_x])
        A.append([sum_x, sum_x2])

        C = []
        C.append(sum_y)
        C.append(sum_xy)

        B = multiply_matrix_vector(inverse_matrix(A), C)
        
        a, b = B[1], B[0]

        return a*self.xp + b