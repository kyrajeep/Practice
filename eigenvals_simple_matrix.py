import numpy as np

def eigenval_calc(matrix1, matrix2):
# takes in two matrices, multiplies them, and outputs eigenvalues of the three matrices.
    matrix3 = np.matmul(matrix1, matrix2)
    a = np.linalg.eig(matrix1)
    b = np.linalg.eig(matrix2)
    c = np.linalg.eig(matrix3)
    return a, b, c
    
if __name__ == "__main__":
    A = np.array([[1, 1, 543], [1, 1, 9000], [1, 2, 3]])
    B = np.array([[1, 1, 5000],[700, 1, 1], [4, 5, 1000]])
    print(eigenval_calc(A,B))

