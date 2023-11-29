import numpy as np
from math import cos, sin
from numpy import linalg  #ako vam treba
np.set_printoptions(precision=5, suppress=True)
 
 # ovde pišete pomocne funkcije
def norm(p):
    norm = sum(list(map(lambda x: x**2, p)))
    return norm

def normalize(p):
    n = norm(p)
    return list(map(lambda x: x/n, p))

def create_pp(p):
    n = len(p)
    A = []

    for i in range(n):
        a = list(map(lambda x: p[i]*x, p))
        # print(a)
        A.append(a)
    return A 

def create_px(p):
    return [[0, -p[2], p[1]], [p[2], 0, -p[0]], [-p[1], p[0], 0]]

def AxisAngle2A(pphi):
    # Rodrigezova f-la
    p = pphi[:3]
    phi = pphi[-1]
    if norm(p) != 1:
        p = normalize(p)
    pp = np.array(create_pp(p))
    px = np.array(create_px(p))
    A = pp + cos(phi)*(np.eye(len(p)) - pp) + sin(phi)*px
    A = np.where(np.isclose(A, 0) , 0.0 , A)  # izbegavanje -0. u rezultatu
    return A
 

# pphi = np.array([1/3, -2/3,  2/3, np.pi/2])
# print(AxisAngle2A(pphi))

