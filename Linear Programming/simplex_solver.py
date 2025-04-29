import numpy as np

def simplex(c, A, b):
    m, n = A.shape
    table = np.zeros((m + 1, n + m + 1))
    table[:m, :n] = A
    table[:m, n:n + m] = np.eye(m)
    table[:m, -1] = b
    table[-1, :n] = -c

    while True:
        if np.all(table[-1, :-1] >= 0):
            break

        col = np.argmin(table[-1, :-1])

        if np.all(table[:-1, col] <= 0):
            raise Exception("Unbounded solution")

        ratios = table[:-1, -1] / table[:-1, col]
        ratios[table[:-1, col] <= 0] = np.inf
        row = np.argmin(ratios)
        pivot = table[row, col]
        table[row, :] /= pivot

        for r in range(m + 1):
            if r != row:
                table[r, :] -= table[r, col] * table[row, :]

    result = np.zeros(n)

    for i in range(n):
        col = table[:, i]

        if np.count_nonzero(col[:-1]) == 1 and np.isclose(col[-1], 0):
            row = np.where(col[:-1] == 1)[0][0]
            result[i] = table[row, -1]

    return result, table[-1, -1]
