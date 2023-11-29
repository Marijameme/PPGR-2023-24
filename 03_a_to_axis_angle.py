import numpy as np
from math import acos, cos, sqrt, radians
np.set_printoptions(precision=5, suppress=True)

 
def ortogonalna(A):
    n = len(A)
    E = np.eye(n)
    AAt = np.array(np.matmul(A, A.T))
    AAt = np.array(np.where(np.isclose(AAt, 0) , 0.0 , AAt))
    same_matrices = np.allclose(E, AAt, rtol=1e-05, atol=1e-08, equal_nan=False)
    return same_matrices

def norm(p):
    norm = sqrt(sum(list(map(lambda x: x**2, p))))
    return norm

def normalize(p):
    n = norm(p)
    return np.array(list(map(lambda x: x/n, p)))

def mesoviti_proizvod(t1, t2, t3):
   t1 = np.array(t1)
   t2 = np.array(t2)
   t3 = np.array(t3)

   return np.cross(t1, t2).dot(t3)

def A2AxisAngle(A):
    if not ortogonalna(A) or abs(np.linalg.det(A) -1) > 1e-5:
        return 'Nije matrica kretanja!'
    
    if np.allclose(np.eye(len(A)), A, rtol=1e-05, atol=1e-08, equal_nan=False):
        return np.array([1,0,0]), 0

    B = np.array(A - np.eye(len(A)))
    p =  np.cross(B[0], B[1])
    pairs = [(0,2), (1,2)]
    if np.allclose(p, [0,0,0], rtol=1e-5, atol=1e-8):
        for pa in pairs:
            p = np.cross(B[pa[0]], B[pa[1]])
            p = normalize(p)
            if not np.allclose(p, [0,0,0], rtol=1e-5, atol=1e-8):
                break

    p = normalize(p)
    u = B[0]
    u = normalize(u)
    up = np.dot(A, u)
    up = normalize(up)

    phi = acos(u.dot(up))
    if mesoviti_proizvod(u, up, p) < 0:
        p = list(map(lambda x: -x, p))
 
    pphi = np.array([p[0],p[1],p[2],phi])  # osa i ugao idu u jedan vektor
    pphi = np.where(np.isclose(pphi, 0) , 0 , pphi)  # izbegavanje -0. u rezultatu
    return pphi
 
A = (1/9)*np.array([[1,-8,-4], [4,4,-7], [8,-1,5]])  #primetite 4->5, matrica A nije ortogonalna
print(A2AxisAngle(A))

A = (1/9)*np.array([[1,-8,-4], [4,4,-7], [8,-1,4]])
print(A2AxisAngle(A))



