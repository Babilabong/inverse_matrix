from colors import bcolors
from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix
import numpy as np

def matrix_inverse(matrix):
    print(bcolors.OKBLUE,
          "=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n", bcolors.ENDC, matrix, bcolors.ENDC)

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    size = matrix.shape[0]
    identity_matrix = np.identity(size)
    step_counter = 0

    for i in range(size):
        matrix, identity_matrix, step_counter = ensure_non_zero_diagonal(matrix, identity_matrix, size, i, step_counter)
        matrix, identity_matrix, step_counter = normalize_diagonal(matrix, identity_matrix, size, i, step_counter)
        matrix, identity_matrix, step_counter = eliminate_below_diagonal(matrix, identity_matrix, size, i, step_counter)

    matrix, identity_matrix, step_counter = eliminate_above_diagonal(matrix, identity_matrix, size, step_counter)

    return identity_matrix

def ensure_non_zero_diagonal(matrix, identity_matrix, size, row_index, step_counter):
    if matrix[row_index, row_index] == 0:
        for swap_index in range(row_index + 1, size):
            if matrix[swap_index, row_index] != 0:
                print(f"Swap rows {row_index + 1} and {swap_index + 1} to make diagonal element non-zero.")
                matrix, identity_matrix = swap_rows(matrix, identity_matrix, size, row_index, swap_index)
                step_counter += 1
                print_step(step_counter, matrix, identity_matrix)
                break
        else:
            raise ValueError("Matrix is singular, cannot find its inverse.")
    return matrix, identity_matrix, step_counter

def swap_rows(matrix, identity_matrix, size, row_index, swap_index):
    elementary_matrix = np.eye(size)
    elementary_matrix[[row_index, swap_index]] = elementary_matrix[[swap_index, row_index]]
    matrix = np.dot(elementary_matrix, matrix)
    identity_matrix = np.dot(elementary_matrix, identity_matrix)
    return matrix, identity_matrix

def normalize_diagonal(matrix, identity_matrix, size, row_index, step_counter):
    if matrix[row_index, row_index] != 1:
        scalar = 1.0 / matrix[row_index, row_index]
        elementary_matrix = scalar_multiplication_elementary_matrix(size, row_index, scalar)
        step_counter += 1
        print_step(step_counter, matrix, identity_matrix)
        matrix = np.dot(elementary_matrix, matrix)
        identity_matrix = np.dot(elementary_matrix, identity_matrix)
    return matrix, identity_matrix, step_counter

def eliminate_below_diagonal(matrix, identity_matrix, size, row_index, step_counter):
    for below_index in range(row_index + 1, size):
        if matrix[below_index, row_index] != 0:
            scalar = -matrix[below_index, row_index]
            elementary_matrix = row_addition_elementary_matrix(size, below_index, row_index, scalar)
            step_counter += 1
            print_step(step_counter, matrix, identity_matrix)
            matrix = np.dot(elementary_matrix, matrix)
            identity_matrix = np.dot(elementary_matrix, identity_matrix)
    return matrix, identity_matrix, step_counter

def eliminate_above_diagonal(matrix, identity_matrix, size, step_counter):
    for col in range(size - 1, 0, -1):
        for row in range(col - 1, -1, -1):
            if matrix[row, col] != 0.0:
                scalar = -matrix[row, col]
                elementary_matrix = row_addition_elementary_matrix(size, row, col, scalar)
                step_counter += 1
                print_step(step_counter, matrix, identity_matrix)
                matrix = np.dot(elementary_matrix, matrix)
                identity_matrix = np.dot(elementary_matrix, identity_matrix)
    return matrix, identity_matrix, step_counter

def print_step(step_counter, matrix, identity_matrix):
    print(f"elementary matrix number: {step_counter}")
    print(f"The matrix after elementary operation:\n {matrix}")
    print(bcolors.OKGREEN, "------------------------------------------------------------------------------------------------------------------", bcolors.ENDC)

def input_square_matrix():
    try:
        size = int(input("Enter the size of the square matrix: "))
        if size <= 0:
            raise ValueError("Size must be a positive integer.")

        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                element = float(input(f"Enter the value for element at position ({i + 1}, {j + 1}): "))
                row.append(element)
            matrix.append(row)

        return np.array(matrix)

    except ValueError as e:
        print(f"Error: {e}")
        return None

# Call the function
square_matrix = input_square_matrix()

if square_matrix is not None:
    print("Entered square matrix:")
    print(square_matrix)

    try:
        A_inverse = matrix_inverse(square_matrix)
        print(bcolors.OKBLUE, "\nInverse of matrix A: \n", A_inverse)
        print("=====================================================================================================================", bcolors.ENDC)
        print("the inverse matrix according numpy function is: \n", np.linalg.inv(square_matrix))
        print("the git link: https://github.com/Babilabong/inverse_matrix/blob/main/new_inverse.py\ngroup:Almog Babila, Hay Carmi, Yagel Batito, Meril Hasid\nstudent:Almog Babila 209477678")

    except ValueError as e:
        print(str(e))