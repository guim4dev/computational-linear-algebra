from src.ex3.solutions.solution import Solution

class Regression(Solution):
    def solve(self):
        sum_x, sum_x2, sum_y, sum_xy = 0, 0, 0, 0
        for i in range(self.n):
            sum_x += self.list_of_points[i][0]
            sum_x2 += self.list_of_points[i][0]**2
            sum_y += self.list_of_points[i][1]
            sum_xy += self.list_of_points[i][0] * self.list_of_points[i][1]

        b = (self.n*sum_xy - sum_x*sum_y) / (self.n*sum_x2 - sum_x*sum_x)
        a = (sum_y - b*sum_x) / self.n

        return a*self.xp + b