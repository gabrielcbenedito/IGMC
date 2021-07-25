import numpy as np
from indexers import SparseRowIndexer, SparseColIndexer
from scipy.sparse import csr_matrix

A = np.zeros((7, 7))
A[0, 5] = 1
A[1, 1] = 2
A[1, 6] = 3
A[2, 3] = 4
A[3, 3] = 5
A[3, 4] = 6
A[3, 5] = 7
A[4, 0] = 8
A[5, 5] = 9
A[6, 3] = 10
A[6, 5] = 11

print(A)
print()

A = csr_matrix(A)

ARowIndexer = SparseRowIndexer(A)

rows = {0, 2}

result = ARowIndexer[list(rows)]

print(result)
print(type(result))
print(result.shape)
