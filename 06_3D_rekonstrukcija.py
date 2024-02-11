import numpy as np
from osmo_teme import osmoteme
from matplotlib import pyplot as plt
np.set_printoptions(precision=12, suppress=True) 

def afine_1(p):
    return np.array([p[0]/p[2], p[1]/p[2]])

def osmotemeD(tacke):
    t1, t2, _, t4,t5, t6, t7, t8 = [np.array([x,y,1]) for x, y in tacke]

    t3t2 = np.cross(t1, t2)
    t7t6 = np.cross(t5, t6)
    t8t5 = np.cross(t8, t7)
    P1 = afine_1(np.cross(t3t2, t7t6))
    P2 = afine_1(np.cross(t3t2, t8t5))
    P3 = afine_1(np.cross(t7t6, t8t5))

    P = (P1+P2+P3)/3.0
    P = np.append(P, 1)

    t6t5 = np.cross(t6, t7)
    t7t8 = np.cross(t7, t8)
    t1t2 = np.cross(t1, t4)
    Q1 = afine_1(np.cross(t6t5, t7t8))
    Q2 = afine_1(np.cross(t6t5, t1t2))
    Q3 = afine_1(np.cross(t7t8, t1t2))
    Q = (Q1+Q2+Q3)/3.0
    np.append(Q, 1)
    Pt1 = np.cross(P, t4)
    Qt3 = np.cross(t2, Q)
    D = np.cross(Pt1, Qt3)
    return [int(D[0]/D[2]), int(D[1]/D[2])]


def jednacina(xl, xd):
    xl = np.array(xl)
    xd = np.array(xd)
    jna = np.concatenate([xd[0]*xl, xd[1]*xl, xd[2]*xl])
    return jna

def homogene(t):
    return np.append(t, 1)

def sredi(tacke):
    return np.array([1,-1,-1])*(np.array([1600,0,0])- tacke)

def fundamentalnaM(L, D):
    A = []
    for l,d in zip(L,D):
        A.append(jednacina(l,d))
    A = np.array(A)
    U, R, V = np.linalg.svd(A)
    F = np.array(V[-1]).reshape(3,3)
    return F

def matricaE(F, K):
    return K.T @ F @ K

def skew_2_v(EC):
    return np.array([EC[1][2], EC[2][0], EC[0][1]])

def sign(num):
    return -1 if num < 0 else 1

def dekomponujE(E):
    Q0 = np.array([[0,-1,0],[1,0,0],[0,0,1]])
    E0 = np.array([[0,1,0],[-1,0,0],[0,0,0]])
    U, S, V = np.linalg.svd(E)
    # if sign(np.linalg.det(U)) != sign(np.linalg.det(V)):
    #     E = -E 
    # if np.linalg.det(U) == -1 and np.linalg.det(V) == -1:
    #     U, V = -U, -V
    EC = U @ E0 @ U.T
    A = U @ Q0 @ V
    C = skew_2_v(EC)

    return A, C

def kamera(E, K):
    A, C = dekomponujE(E)
    C1 = K  @ -A.T @ C
    C1 = np.array(C1)
    A = K @ A.T
    # reshape(-1,1) pretvara 1D niz u 2D kolonu
    kam1 = np.hstack((A, C1.reshape(-1,1)))
    return kam1

def afine(t):
    if 0 != t[3]:
        return [t[0]/t[3], t[1]/t[3], t[2]/t[3]]
    return [t[0], t[1], t[2], t[3]]

def triangulacija(kam1, kam2, xl, xd):
    kam1 = np.array(kam1)
    kam2 = np.array(kam2)
    xl = np.array(xl)
    xd = np.array(xd)
    arr = [[xl[1]*kam1[2]-kam1[1]],
        [-xl[0]*kam1[2]+kam1[0]],
        [xd[1]*kam2[2]-kam2[1]],
        [-xd[0]*kam2[2]+kam2[0]]]
    A = np.vstack(arr)
    U, S, V = np.linalg.svd(A)
    pt = V[3]
    pt = (1/pt[3])*pt
    pt = np.array(afine(pt))
    pt = np.where(np.isclose(pt, 0) , 0 , pt)  # izbegavanje -0. u rezultatu
    return pt

# def nacrtaj(tacke, ivice):
#     ax = plt.figure().add_subplot(projection='3d')
#     for x,y,z in tacke:
#         ax.scatter(x, y, z)
#     for p, k in ivice:
#         ax.plot([tacke[p][0], tacke[k][0]], [tacke[p][1], tacke[k][1]], [tacke[p][2], tacke[k][2]])
#     plt.show()

#  Plotuje 3D scenu
def plot(tacke):

    # Crta 3D figuru čije su stranice prosleđene
    def nacrtaj(ax, tacke, stranice, c):

        for i in range(len(stranice)):
            ax.plot([tacke[stranice[i][0]][0], tacke[stranice[i][1]][0]],
                    [tacke[stranice[i][0]][1], tacke[stranice[i][1]][1]],
                    [tacke[stranice[i][0]][2], tacke[stranice[i][1]][2]], color = c)

    fig = plt.figure("Scena")
    fig.set_figheight(7)
    fig.set_figwidth(10)
    fig.subplots_adjust(top = 1, bottom = 0, left = 0, right = 1)
    ax = plt.axes(projection = '3d')
    ax.set_xlabel("X", color = 'g')
    ax.set_ylabel("Y", color = 'g')
    ax.set_zlabel("Z", color = 'g')

    # ax.set_xlim(-2,1)
    # ax.set_ylim(-2,1)
    # ax.set_zlim(0.5,3.5)
    # ax.set_box_aspect((1, 1, 1))

    # Tačke
    for i in range(len(tacke)):
        oznaka, broj, boja = 'P', i + 1, 'r'
        if i >= 8 and i < 16:
            oznaka, broj, boja = 'Q', broj % 8, 'm'
        if i >= 16:
            oznaka, broj, boja = 'R', broj % 8, 'b'
        ax.text(tacke[i][0], tacke[i][1], tacke[i][2], oznaka + str(broj), color = boja, fontsize = 10)
        ax.plot(tacke[i][0], tacke[i][1], tacke[i][2], boja + '.')

    karte = np.array([[0,1], [1,2], [2,3], [3,0], [4,5], [5,6], [6,7], [7,4], [0,4], [1,5], [2,6], [3,7]])
    nacrtaj(ax, tacke, karte, 'r')

    sok = np.array([x+8 for x in karte])
    nacrtaj(ax, tacke, sok, 'm')

    mleko = np.array([x+16 for x in karte])
    nacrtaj(ax, tacke, mleko, 'b')

    plt.show()


# leva kamera
Kl = np.array([[1173,500],[1116,518],[982,253],[1048,254],[1257,321],[1186,321],[1030,45],[1087,32]])
Sl = np.array([[845,372],[681,488],[569,390],[735,291],[856,292],[678,421],[559,313],[736,195]])
Ml = np.array([[686,768],[587,993],[230,864],[376,656],[678,674],[559,931],[157,787],[317,553]])

# Kl[3] = osmoteme(Kl)
# Sl[3] = osmoteme(Sl)
# Ml[3] = osmoteme(Ml)
# print(Kl[3], Sl[3], Ml[3])

L = np.concatenate((Kl, Sl, Ml))
L = np.array([homogene(l) for l in L])
L = sredi(L)
L8 = np.array([L[0], L[1], L[2], L[7], L[8], L[9], L[15], L[16]])

ivice = np.array([[1,2], [2,3], [3,4],[4,1], [5,6], [6,7], [7,8],[8,5], [1,5], [2,6], [3,7], [4,8],
                  [9,10],[10,11],[11,12],[12,9], [13,14],[14,15],[15,16],[16,13],[9,13],[10,14],[11,15],[12,16],
                  [17,18],[18,19],[19,20],[20,17],[21,22],[22,23],[23,24],[24,21],[17,21],[18,22],[19,23],[20,24]])
for i in range(len(ivice)):
    ivice[i][0] -= 1
    ivice[i][1] -= 1
# desna kamera
Kd = np.array([[995,931],[933,873],[1260,640],[1314,677],[1049,785],[968,699],[1394,409],[1468,471]])
Sd = np.array([[990,525],[751,436],[837,314],[1055,396],[1011,451],[750,358],[835,223],[1081,305]])
Md = np.array([[431,540],[186,541],[206,276],[471,286],[362,390],[81,392],[169,119],[410,120]])

# Kd[3] = osmoteme(Kd)
# Sd[3] = osmoteme(Sd)
# Md[3] = osmoteme(Md)
# print(Kd[3], Sd[3], Md[3])
# Kd[2], Kd[3] = Kd[3], Kd[2]
# Sd[2], Sd[3] = Sd[3], Sd[2]
# Md[2], Md[3] = Md[3], Md[2]

D = np.concatenate((Kd, Sd, Md))
D = [homogene(d) for d in D]
D = sredi(D)
D8 = np.array([D[0], D[1], D[2], D[7], D[8], D[9], D[15], D[16]])

K = np.array([[1300,0,800],[0,1300,600],[0,0,1]])
F = fundamentalnaM(L, D)
E = matricaE(F, K)
A, C = dekomponujE(E)
kam1 = kamera(E, K)
kam2 = np.array([[K[0][0], K[0][1], K[0][2], 0],
                [0, K[1][1], K[1][2], 0],
                [0, 0, K[2][2], 0]])

# radi dobro
def test_triangilacije():
    T1 = [[-2,-1,0,2], [-3,0,1,0],[-1,0,0,0]]
    T2 = [[2,-2,0,-2],[0,-3,2,-2],[0,-1,0,0]]
    M1 = [5,3,1]
    M2 = [-2,1,1]
    print(triangulacija(T1,T2,M1, M2))

tacke3D = []
for t1, t2 in zip(L, D):
    pt = triangulacija(kam1, kam2, t1, t2)
    tacke3D.append(pt)
tacke3D = np.array(tacke3D)
E0 = np.array([[0,1,0],[-1,0,0],[0,0,0]])
# print("F: ")
# print(F)
# print("E: ")
# print(E)
# print("E0:")
# print(E0)
# print("A:")
# print(A)
# print("T1:")
# print(kam1)
# print("T2:")
# print(kam2)
# print("Rekonstruisane tacke:")
# print(tacke3D)
plot(tacke3D)
