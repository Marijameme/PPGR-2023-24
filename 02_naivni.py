import numpy as np
from itertools import combinations

np.set_printoptions(precision=5, suppress=True)
 
 # ovde pišete pomocne funkcije
def mesoviti_proizvod(t1, t2, t3):
   t1 = np.array(t1)
   t2 = np.array(t2)
   t3 = np.array(t3)

   return np.cross(t1, t2).dot(t3)

def opsti_polozaj(tacke) -> bool:
   for t1, t2, t3 in combinations(tacke, 3):
      if mesoviti_proizvod(t1, t2, t3) == 0:
         return False
   return True

def preslikaj(tacke):
   jna_1 = np.array([tacke[0][0], tacke[1][0], tacke[2][0]])
   jna_2 = np.array([tacke[0][1], tacke[1][1], tacke[2][1]])
   jna_3 = np.array([tacke[0][2], tacke[1][2], tacke[2][2]])
   koef = np.array([jna_1, jna_2, jna_3])
   b = np.array(tacke[3])
   x = np.linalg.solve(koef, b)
   tacke = np.array(tacke[:3])
   res = np.array([tacke[0]*x[0], tacke[1]*x[1], tacke[2]*x[2]])
   res = res.transpose()
   
   return res

def sredi_matricu(f):
   eps = 1e-15
   koef = f[-1][-1]
   f = f/koef
   for i in range(len(f)):
      for j in range(len(f[0])):
         if abs(f[i][j]) <= eps:
            f[i][j] = abs(f[i][j])
   return f
 
def naivni(origs, imgs):
   if not opsti_polozaj(origs):
      return "Losi originali!"
   if not opsti_polozaj(imgs):
      return "Lose slike!"

   h = preslikaj(imgs)
   g = preslikaj(origs)
   f = np.dot(h, np.linalg.inv(g))
   f = sredi_matricu(f)
   return f



