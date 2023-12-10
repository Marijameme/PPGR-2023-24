import numpy as np
from matplotlib import pyplot as plt
import importlib
centar = importlib.import_module('05_centar')
kameraK = importlib.import_module('05_kameraK')
kameraA = importlib.import_module('05_kameraA')
matrica_kamere = importlib.import_module('05_matricaKamere')


org =  np.array([1,-1,-1])*(np.array([1600,0,0])- np.array([[744,184, 1],[1108,384, 1],[717,622,1],[364,334,1], [437,693,1],[704,957,1],[1015,707,1]]))
img = np.array([[0,0,3,1],[0,3,3,1],[3,3,3,1],[3,0,3,1],[3,0,0,1],[3,3,0,1],[0,3,0,1]])

T = matrica_kamere.matricaKamere(org, img)
print('Matrica kamere:')
print(T)
print('\nPozicija centra kamere:')
C = centar.centar(T)
print(C)
print('\nSpoljasnja matrica kamere:')
A = kameraA.kameraA(T)
print(A)
print('\nMatrica kalibracije kamere:')
K = kameraK.kameraK(T)
print(K)

n_voxels = np.zeros((3, 3, 3), dtype=bool)
for i in range(3):
    for j in range(3):
        for k in range(3):
            if (i+j+k)%2 == 1:
                n_voxels[i,j,k] = True
filled = np.ones(n_voxels.shape)
ax = plt.figure().add_subplot(projection='3d')
facecolors = np.where(n_voxels, 'red', 'yellow')
ax.voxels(filled, facecolors=facecolors)

ax.quiver(0,0,0, 4,0,0, color='red', label='x', alpha=0.9)
ax.text(4.2, 0, 0, s="X")
ax.quiver(0,0,0, 0,4,0, color='green', label='y', alpha=0.9)
ax.text(0, 4.2, 0, s="Y")
ax.quiver(0,0,0, 0,0,4, color='blue', label='z', alpha=0.9)
ax.text(0, 0, 4.2, s="Z")

ax.quiver(C[0], C[1], C[2], A[0][0], A[0][1], A[0][2], color='red', label='x', alpha=0.9)
ax.quiver(C[0], C[1], C[2], A[1][0], A[1][1], A[1][2], color='green', label='y', alpha=0.9)
ax.quiver(C[0], C[1], C[2], A[2][0], A[2][1], A[2][2], color='blue', label='z', alpha=0.9)
ax.scatter(C[0], C[1], C[2])
ax.text(C[0]+0.2, C[1]+0.2, C[2]+0.2, s="C")

d =  (7.6/35)*26

plt.show()