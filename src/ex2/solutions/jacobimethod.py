from tabnanny import check
from src.ex2.solutions.solution import Solution
from src.utils.matrix import calc_determinant, is_simetric, get_biggest_element_not_in_diagonal, calculate_p_matrix, multiply_matrixes, transpose_matrix

class JacobiMethod(Solution):
    def solve(self):
        
        if(not is_simetric(self.A)):
            raise Exception("Matriz A deve ser simétrica para realizar o Método de Jacobi")
        
        X = [[float(i == j) for j in range(self.order)] for i in range(self.order)]
        
        element_ij = get_biggest_element_not_in_diagonal(self.A)
        while (abs(self.A[element_ij[0]][element_ij[1]]) > self.maxTolerance):
            P = calculate_p_matrix(self.A, element_ij)
            Pt = transpose_matrix(P)
            self.A = multiply_matrixes(Pt, multiply_matrixes(self.A, P))
            X = multiply_matrixes(X, P)
            element_ij = get_biggest_element_not_in_diagonal(self.A)
        
        values = []
        for i in range(self.order):
            values.append(self.A[i][i]) 


        determinant = None
        if self.calc_determinant:
            determinant = calc_determinant(self.A)
            print('Determinante:', determinant)
                
        return {
        'vectors': X,
        'eigenvalues': values,
        'determinant': determinant
    }