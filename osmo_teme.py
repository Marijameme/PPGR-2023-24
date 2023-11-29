import numpy as np

def osmoteme(tacke):
    t5, t6, t7, t8, t1, t2, t3 = [np.array([x,y,1]) for x, y in tacke]
    
    t3t2 = np.cross(t3, t2)
    t7t6 = np.cross(t7, t6)
    t8t5 = np.cross(t8, t5)
    P1 = np.cross(t3t2, t7t6)
    P2 = np.cross(t3t2, t8t5)
    P3 = np.cross(t7t6, t8t5)
    P = (P1+P2+P3)/3.0

    t6t5 = np.cross(t6, t5)
    t7t8 = np.cross(t7, t8)
    t1t2 = np.cross(t1, t2)
    Q1 = np.cross(t6t5, t7t8)
    Q2 = np.cross(t6t5, t1t2)
    Q3 = np.cross(t7t8, t1t2)
    Q = (Q1+Q2+Q3)/3.0

    Pt1 = np.cross(P, t1)
    Qt3 = np.cross(t3, Q)
    D = np.cross(Pt1, Qt3)


    return [int(D[0]/D[2]), int(D[1]/D[2])]

osmoteme([[32, 70], [195, 144], [195, 538], [30, 307], [251, 40], [454, 78], [455, 337]])