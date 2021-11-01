import numpy as np
from fraction import Fraction as fr


def get_leading_one(row: np.array):
    for idx, val in enumerate(row):
        if val != fr(0,1):
            return idx
    return len(row)


def rref(matrix: np.array):
    n, m = matrix.shape

    # Iterate through the diagonal of the matrix
    for i in range(min(m, n)):
        leading_one_index = get_leading_one(matrix[i])

        if leading_one_index == m:
            continue

        leading_one = matrix[i][leading_one_index]
        if leading_one != fr(1, 1):
            matrix[i] /= leading_one

        current_row = matrix[i]

        for j in range(n):
            if j == i:
                continue

            factor = matrix[j][leading_one_index]  # /leading_one
            matrix[j] -= current_row * factor

    res = np.empty((n,m))
    for i in range(n):
        for j in range(m):
            res[i,j]=int(matrix[i,j])

    print(res)

    return matrix

if __name__ == "__main__":

    A = np.array([
        [2, 1, 7, -7,2],
        [-3, 4, -5, -6,3],
        [1, 1, 4, -5,2]
    ])

    n, m = A.shape

    B = np.empty((n,m), dtype="object")

    for i in range(n):
        for j in range(m):
            B[i, j] = fr(A[i, j], 1)

    rref(B) 
