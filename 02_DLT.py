import numpy as np
from numpy import linalg  #zbog SVD algoritma
np.set_printoptions(precision=5, suppress=True)
 
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
