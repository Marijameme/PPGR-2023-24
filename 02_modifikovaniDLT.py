import numpy as np
from math import sqrt
from numpy import linalg  #zbog SVD algoritma
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

def sredi_matricu(f):
   eps = 1e-15
   koef = f[-1][-1]
   f = f/koef
   for i in range(len(f)):
      for j in range(len(f[0])):
         if abs(f[i][j]) <= eps:
            f[i][j] = abs(f[i][j])
   return f        
 
def DLT(origs, imgs):
    A = []
    for i in range(len(origs)):
        x1, x2, x3 = origs[i]
        x1p, x2p, x3p = imgs[i]
        A.append([0,0,0, -x3p*x1, -x3p*x2, -x3p*x3, x2p*x1, x2p*x2, x2p*x3])
        A.append([x3p*x1, x3p*x2, x3p*x3, 0, 0, 0, -x1p*x1, -x1p*x2, -x1p*x3])

    A = np.array(A)
    U, D, V = np.linalg.svd(A)
    mat = np.array(V[8]).reshape(3,3)
    mat = sredi_matricu(mat)
    return mat
 
def DLTwithNormalization(origs, imgs):
    norm_mat_orgs = np.array(normMatrix(origs))
    origs = [np.dot(norm_mat_orgs, o) for o in origs]
    norm_mat_imgs = np.array(normMatrix(imgs))
    imgs = [np.dot(norm_mat_imgs, i) for i in imgs]
    # print(imgs)
    D = DLT(origs, imgs)
    mat = np.linalg.inv(norm_mat_imgs).dot(D).dot(norm_mat_orgs)
    mat = sredi_matricu(mat)
    return mat


