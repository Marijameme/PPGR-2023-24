import numpy as np
from numpy import linalg
from math import acos, sqrt, degrees
np.set_printoptions(precision=5, suppress=True) 

# pomocne funkcije, ako treba
def normalizuj(q):
    return q/linalg.norm(q)
def tacka(p):
    return p[0] == 0 and p[1] == 0 and p[2] == 0

def Q2AxisAngle(q):
    q = normalizuj(q)
    w = q[-1]
    if w < 0:
        q = -q
    phi = 2*np.arccos(q[-1])
    if np.isclose(abs(w), 1) or tacka(q[:-1]):
        return np.array([1,0,0,0])
    else:
        px, py, pz = normalizuj(q[:-1])
 
    pphi = np.array([px,py,pz,degrees(phi)])  # osa i ugao idu u jedan vektor. Naravno, vas kod moze biti drugaciji
    pphi = np.where(np.isclose(pphi, 0) , 0 , pphi)  # izbegavanje -0. u rezultatu
    return pphi
 

# identitet
q = np.array([0,sqrt(3)/2,0,-0.5])
print(Q2AxisAngle(q))