import numpy as np
from numpy import linalg
from math import sqrt
np.set_printoptions(precision=5, suppress=True)
 
def afine(tacka):
    x1, x2, x3 = tacka
    return [x1/x3, x2/x3, 1]

def norma(tacka):
    x1, x2, _ = tacka
    return sqrt(x1**2+x2**2)

def skaliranje(lam):
    return np.array([[lam, 0, 0], [0, lam, 0], [0, 0, 1]])

def translacija(tacka):
    x1, x2, _ = tacka
    return np.array([[1, 0, -x1], [0,1,-x2], [0,0,1]])

def normMatrix(points):
    points = np.array(points)
    points = np.apply_along_axis(afine, 1, points)
    T = np.mean(points, axis=0)
    translirane = np.array([np.array(P-T) for P in points])
    norme = np.apply_along_axis(norma, 1, translirane)
    rast = np.mean(norme)
    lam = sqrt(2)/rast
    S = skaliranje(lam)
    T = translacija(T)
    mat = np.dot(S, T)
    return mat

