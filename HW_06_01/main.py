from Matrix2D import Matrix2D
from Vector2D import Vector2D
from Solver import Solver

def read_Matrix(file_path):
    matrix_arr = []
    with open(file_path, "r") as f:
        for line in f:
            A = Matrix2D(*list(map(int, line.split())))
            matrix_arr.append(A)
    return matrix_arr

def read_Vector(file_path):
    vector_arr = []
    with open(file_path, 'r') as f:
        for line in f:
            b = Vector2D(*list(map(int, line.split())))
            vector_arr.append(b)
    return vector_arr


def results(file_path, matrix_arr, vector_arr):
    with open(file_path, 'w') as f:
        for i in range(len(matrix_arr)):
            res = Solver(matrix_arr[i], vector_arr[i])
            print(res.solve(), file = f)


matrix_arr = read_Matrix('matrix_coefficients.txt')
vector_arr = read_Vector('rhs_values.txt')

results('output.txt', matrix_arr, vector_arr)