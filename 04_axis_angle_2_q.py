import numpy as np
from numpy import linalg
from math import cos, sin, pi 
np.set_printoptions(precision=5, suppress=True) 

# pomocne funkcije, ako treba

def normalizuj(p):
    return p/linalg.norm(p)

def AxisAngle2Q(pphi):
    p = pphi[:-1]
    phi = pphi[-1]

    # identitet je ako je ugao rotacije 2PI ili 0
    if abs(phi - 2*pi) < 1e-5 or np.isclose(phi, 0):
        return [0,0,0,1]
    
    w = cos(phi/2)
    p = normalizuj(p)
    (x,y,z) = sin(phi/2)*p
    
    q = np.array([x,y,z,w])  # naravno, ne mora da bude ovako
    q = np.where(np.isclose(q, 0) , 0 , q)  # izbegavanje -0. u rezultatu
    return q
 

pphi = np.array([1, 0,0, (np.pi)/2])
print(AxisAngle2Q(pphi))
pphi = np.array([1, 1,1, (2*np.pi)/3])
print(AxisAngle2Q(pphi))
pphi = np.array([1,0,0, (2*pi)])
print(AxisAngle2Q(pphi))