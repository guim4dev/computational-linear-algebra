class Solution:

    def __init__(self, t1, t2, maxTolerance, **kwargs):
        self.t1 = t1
        self.t2 = t2
        self.maxTolerance = maxTolerance

    def solve(self):
        raise RuntimeError('Not implemented')

    def F(self, X):
        f1 = 2*X[1]**2 + X[0]**2 + 6*X[2]**2 - 1
        f2 = 8*X[1]**2 + 6*X[1]*X[0]**2 + 36*X[1]*X[0]*X[2] + 108*X[1]*X[2]**2 - self.t1
        f3 = 60*X[1]**4 + 60*(X[1]**2)*(X[0]**2) + 576*(X[1]**2)*X[0]*X[2] + 2232*(X[1]**2)*(X[2]**2) + 252*(X[2]**2)*(X[0]**2) + 1296*(X[2]**3)*X[0] \
            + 3348*X[2]**4 + 24*(X[0]**3)*X[2] + 3*X[0] - self.t2
        
        return [f1, f2, f3]
    
    def Jacobian(self, X):
        df1 = [2*X[0], 4*X[1], 12*X[2]]
        
        df2 = [12*X[1]*X[0] + 36*X[1]*X[2], \
               16*X[1] + 6*X[0]**2 + 36*X[0]*X[2] + 108*X[2]**2, \
               36*X[0]*X[1] + 216*X[1]*X[2]]
        
        df3c1 = 1296*X[2]**3 + 504*X[0]*X[2]**2 + 576*X[2]*X[1]**2 + 72*X[2]*X[0]**2 + 120*X[0]*X[1]**2 + 3
        df3c2 = 240*X[1]**3 + 120*X[1]*X[0]**2 + 1152*X[0]*X[1]*X[2] + 4464*X[1]*X[2]**2
        df3c3 = 24*X[0]**3 + 504*X[2]*X[0]**2 + 576*X[0]*X[2]**2 + 3888*X[0]*X[2]**2 + 4464*X[2]*X[1]**2 + 13392*X[2]**2
        df3 = [df3c1, df3c2, df3c3]
        
        return [df1, df2, df3]