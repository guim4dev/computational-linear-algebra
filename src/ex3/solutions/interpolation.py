from src.ex3.solutions.solution import Solution

class Interpolation(Solution):
    def solve(self):
        yp = 0
        for i in range(self.n):
            p = 1
            for j in range(self.n):
                if i != j:
                    p = p * (self.xp - self.list_of_points[j][0]) / (self.list_of_points[i][0] - self.list_of_points[j][0]) # x - xi / xi - xj
            
            yp = yp + p * self.list_of_points[i][1] #yp + p * yi

        return yp