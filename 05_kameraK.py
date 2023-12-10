import numpy as np
from numpy import linalg
np.set_printoptions(precision=5, suppress=True) 

# donje trougaona
def kameraK(T):
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

    K = linalg.inv(R)
    if K[2][2]:
        K = K/K[2][2]
    K = np.where(np.isclose(K, 0) , 0.0 , K)  # izbegavanje -0. u rezultatu
    return K

# T = np.array([[-5, 2, 0, 1], [3, 0, 2, -9], [1, 0, 0, -1]])
# # print(kameraK(T))

# A = np.array([[-2, 3, 0, 7], [-3, 0, 3, -6], [1, 0, 0, -3]])
# # print(kameraK(A))

# T = np.array([[-2,3,0,7], [-3,0,3,-6], [1,0,0,-2]])
# print(kameraK(T))

# [[ 3.  0. -2.]
#  [ 0.  3. -3.]
#  [ 0.  0.  1.]]