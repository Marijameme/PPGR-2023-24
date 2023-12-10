import numpy as np
from numpy import linalg
import math
np.set_printoptions(precision=5, suppress=True) 
 
 # ovde pišete pomocne funkcije
 
def matricaKamere(pts2D, pts3D):
    A = []
    for i in range(len(pts2D)):
        x1, x2, x3 = pts2D[i]
        xp1, xp2, xp3, xp4 = pts3D[i]
        A.append([0, 0, 0, 0, -x3*xp1, -x3*xp2, -x3*xp3, -x3*xp4, x2*xp1, x2*xp2, x2*xp3, x2*xp4])
        A.append([x3*xp1, x3*xp2, x3*xp3, x3*xp4, 0, 0, 0, 0, -x1*xp1, -x1*xp2, -x1*xp3, -x1*xp4])
    A = np.array(A)

    _, _, V = linalg.svd(A)
    T = np.array(V[-1]).reshape(3, 4)
    T /= T[2][3]
    
    T = np.where(np.isclose(T, 0) , 0.0 , T)
    return T

# pts2D = np.array([[12, 61, 31], [1, 95, 4], [20, 82, 19], [56, 50, 55], [32, 65, 84], [46, 39, 16], [67, 63, 78]])
# pts3D = np.array([[44, 61, 31, 99], [17, 84, 40, 45], [20, 59, 65, 3], [37, 81, 70, 82], [7, 95, 8, 29], [31, 61, 91, 37], [82, 99, 80, 7]])
# print(matricaKamere(pts2D,pts3D))
