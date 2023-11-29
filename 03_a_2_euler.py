import numpy as np
import math
from numpy import linalg  #ako vam treba
np.set_printoptions(precision=5, suppress=True)  # formatiranje izlaza na 5 decimala

 
def ortogonalna(A):
    n = len(A)
    E = np.eye(n)
    AAt = np.array(np.dot(A, A.T))
    AAt = np.array(np.where(np.isclose(AAt, 0) , 0.0 , AAt))
    same_matrices = np.allclose(E, AAt, rtol=1e-05, atol=1e-08, equal_nan=False)
    return same_matrices
 
def A2Euler(A):
    if not ortogonalna(A) or not np.allclose(np.linalg.det(A), 1, rtol=1e-5):
        return 'Nije matrica kretanja!'
    
    if abs(A[2][0]) != 1:
        theta = math.asin(-A[2][0])
        psi = math.atan2(A[1][0], A[0][0])
        phi = math.atan2(A[2][1], A[2][2])

    elif np.allclose((A[2][0]), 1, rtol=1e-5):
        theta = -math.pi / 2
        phi = 0
        psi = math.atan2(-A[0][1], A[1][1])

    elif np.allclose((A[2][0]), -1, rtol=1e-5):
        theta = math.pi / 2
        phi = 0
        psi = math.atan2(-A[0][1], A[1][1])
    uglovi = np.array([psi, theta, phi])
    uglovi = np.where(np.isclose(uglovi, 0) , 0 , uglovi),    
    return uglovi[0]
 
A = np.array([[0,0,-1], [0, -1, 0], [-1, 0, 0]])
print(A2Euler(A))
A = np.array([[0,1,0], [0,0,1], [1,0,0]])	
print(A2Euler(A))
A = np.array([[0,1,0], [0,0,1], [1,0,0]])
print(A2Euler(A))

