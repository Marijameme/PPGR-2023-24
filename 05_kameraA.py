import numpy as np
from numpy import linalg
from math import acos, sqrt, degrees
np.set_printoptions(precision=5, suppress=True) 

# ortonormirana
def kameraA(T):
    T0 = np.delete(T, 3, 1)
    if linalg.det(T0) < 0:
        T0 = -T0
    Q, R = linalg.qr(linalg.inv(T0)) 

    if R[0][0] < 0:
        R = np.diag([-1, 1, 1])@R
        Q = Q@np.diag([-1, 1, 1])
    if R[1][1] < 0:
        R = np.diag([1, -1, 1])@R
        Q = Q@np.diag([1, -1, 1])
    if R[2][2] < 0:
        R = np.diag([1, 1, -1])@R
        Q = Q@np.diag([1, 1, -1])

    A = np.transpose(Q)
    A = np.where(np.isclose(A, 0) , 0.0 , A)  # izbegavanje -0. u rezultatu
    return A


# T = np.array([[-2,3,0,7], [-3,0,3,-6], [1,0,0,-2]])
# # print(kameraA(T))

# T2 = np.array([[-40.76114 , 96.88137  , 5.02608 , 257.87105],
#  [-80.7022 , -30.26509 , 64.822  , 433.86004],
#  [ -0.02538 , -0.00392 , -0.01387 ,  1.     ]])
# print(kameraA(T2))