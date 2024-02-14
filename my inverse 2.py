from colors import bcolors
from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix
import numpy as np

def matrix_inverse(matrix):
    counter = 0
    print(bcolors.OKBLUE,
          "=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n", bcolors.ENDC,matrix, bcolors.ENDC)

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)

    for i in range(n):
        if matrix[i, i] == 0:
            # If there's a zero on the diagonal, find a non-zero element in the same column below
            found_nonzero = False
            for j in range(i + 1, n):
                if matrix[j, i] != 0:
                    found_nonzero = True
                    # Swap rows to make the diagonal element non-zero
                    print(f"Swap rows {i+1} and {j+1} to make diagonal element non-zero.")
                    elementary_matrix = np.eye(n)
                    elementary_matrix[[i, j]] = elementary_matrix[[j, i]]
                    counter += 1
                    print("elementary matrix number: ",counter)
                    print(f"elementary matrix to swap rows {i+1} and {j+1}:\n {elementary_matrix} \n")
                    matrix = np.dot(elementary_matrix, matrix)
                    identity = np.dot(elementary_matrix, identity)
                    break

            if not found_nonzero:
                raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            counter += 1
            print("elementary matrix number: ", counter)
            print(f"elementary matrix to make the diagonal element 1 :\n {elementary_matrix} \n")
            matrix = np.dot(elementary_matrix, matrix)
            identity = np.dot(elementary_matrix, identity)
            print(f"The matrix after elementary operation :\n {matrix}")
            print(bcolors.OKGREEN,"------------------------------------------------------------------------------------------------------------------",bcolors.ENDC)

        # Zero out the elements above and below the diagonal
        for j in range(i+1,n):
            if i != j and matrix[j,i] != 0:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                counter += 1
                print("elementary matrix number: ", counter)
                print(f"elementary matrix for R{j+1} = R{j+1} + ({scalar}R{i+1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                identity = np.dot(elementary_matrix, identity)
                print(f"The matrix after elementary operation :\n {matrix}")
                print(bcolors.OKGREEN,
                      "------------------------------------------------------------------------------------------------------------------",
                      bcolors.ENDC)

        #if(np.all(np.triu(matrix) == matrix)):
    for col in range(n-1,0,-1):
        for row in range(n-2,-1,-1):
            if row != col and matrix[row][col] != 0.0:
                scalar = -matrix[row][col]
                elementary_matrix = row_addition_elementary_matrix(n, row, col, scalar)
                counter += 1
                print("elementary matrix number: ", counter)
                print( f"elementary matrix for R{col + 1} = R{col + 1} + ({scalar}R{row + 1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                identity = np.dot(elementary_matrix, identity)
                print(f"The matrix after elementary operation :\n {matrix}")
                print(bcolors.OKGREEN, "------------------------------------------------------------------------------------------------------------------",bcolors.ENDC)


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
        print("the inverse matrix according numpy function is: \n", np.linalg.inv(square_matrix))
        print("the git link: https://github.com/Babilabong/inverse_matrix\ngroup:Almog Babila, Hay Carmi, Yagel Batito, Meril Hasid\nstudent:Almog Babila 209477678")

    except ValueError as e:
        print(str(e))