import numpy as np
from numpy import linalg
from math import acos, sqrt, degrees
np.set_printoptions(precision=5, suppress=True) 

def centar(A):
    # brisemo kolone redom i nalazimo determinante
    A1 = np.linalg.det(np.delete(A, 0, 1))
    A2 = np.linalg.det(np.delete(A, 1, 1))
    A3 = np.linalg.det(np.delete(A, 2, 1))
    A4 = np.linalg.det(np.delete(A, 3, 1))

    C = (-1/A4)*np.array([A1, -A2, A3, -A4])
    C = np.where(np.isclose(C, 0) , 0.0 , C)  # izbegavanje -0. u rezultatu
    return C

# # za ovaj primer radi
# A = np.array([[-5, 2, 0, 1], [3, 0, 2, -9], [1, 0, 0, -1]])
# print(centar(A))


# A = np.array([[-2, 3, 0, 7], [-3, 0, 3, -6], [1, 0, 0, -3]])
# print(centar(A))

# T = np.array([[-2,3,0,7], [-3,0,3,-6], [1,0,0,-2]])
# print(centar(T))