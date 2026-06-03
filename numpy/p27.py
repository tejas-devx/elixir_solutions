import numpy as np

a = np.array([[4, 2],
              [1, 3]])

eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors)