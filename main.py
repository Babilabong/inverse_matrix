from colors import bcolors
from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix
import numpy as np

def inverse_test(matrix,invMatrix):
    size = matrix.shape[0]
    newMatrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for z in range(size):
                newMatrix[i][j] += matrix[i][z]*invMatrix[z][j]

    if newMatrix == [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]:
        print("check is done")
        print(newMatrix)
    else:
        print("fail in check")
        print(newMatrix)



def matrix_inverse(matrix):
    print(bcolors.OKBLUE,
          "=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n",
          matrix, bcolors.ENDC)

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)

    for i in range(n):
        if matrix[i, i] == 0:
            # Perform pivot operation to avoid division by zero
            pivot_row = i + 1
            while pivot_row < n and matrix[pivot_row, i] == 0:
                pivot_row += 1

            if pivot_row == n:
                raise ValueError("Matrix is singular, cannot find its inverse.")

            # Swap rows to make the diagonal element non-zero
            elementary_matrix = row_addition_elementary_matrix(n, i, pivot_row, 1.0)
            matrix = np.dot(elementary_matrix, matrix)
            identity = np.dot(elementary_matrix, identity)

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            matrix = np.dot(elementary_matrix, matrix)
            identity = np.dot(elementary_matrix, identity)

        # Zero out the elements above and below the diagonal
        for j in range(n):
            if i != j:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                matrix = np.dot(elementary_matrix, matrix)
                identity = np.dot(elementary_matrix, identity)

    return identity

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
        inverse_test(square_matrix, A_inverse)

    except ValueError as e:
        print(str(e))

