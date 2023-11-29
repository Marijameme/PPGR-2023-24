import numpy as np

class Kvaternion:
    def __init__(self, x, y, z,w ) -> None:
        self.x = x
        self.y = y
        self.z = z 
        self.w = w

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w
        return Kvaternion(x, y, z,w)
    
    def __mul__(self, other):
        u = np.array([self.x, self.y, self.z])
        v = np.array([other.x, other.y, other.z])
        x, y, z = np.cross(u, v) +self.w*v + other.w*u
        w = self.w*other.w - u.dot(v)

        return Kvaternion(x, y, z, w)
    
    def __str__(self) -> str:
            string = ''
            if self.x != 1:
                 string += f'{self.x}*i'

            if self.y < 0:
                 string += f' - {abs(self.y)}*j'
            elif self.y != 1:
                 string += f' + {self.y}*j'
            else:
                 string += ' + j'

            if self.z < 0:
                 string += f' - {abs(self.z)}*k'
            elif self.z != 1:
                 string += f' + {self.z}*k'
            else:
                 string += ' + k'

            if self.w < 0:
                 string += f' - {abs(self.w)}'
            elif self.w != 0:
                 string += f' + {self.w}'

            return string
   
    def konjugacija(self):
        return Kvaternion(-self.x, -self.y, -self.z, self.w)
    
    def norma_2(self):
        return sum([self.x**2, self.y**2, self.z**2, self.w**2])
    
    def inverz(self):
        n = self.norma_2()
        i = self.konjugacija()
        return Kvaternion(i.x/n, i.y/n, i.z/n, i.w/n)
    
    def mnozenje_skalarom(self, x):
         return Kvaternion(x*self.x, x*self.y, x*self.z, x*self.w)
q1 = Kvaternion(1, 3, 1, -7)
q2 = Kvaternion(-5, -5, 7, 1)
q3 = Kvaternion(1,5,3,1)
# print(q1+q2)
# print(q1*q2)
# print(q2*q1)
se = Kvaternion(0,0,0,6)
print(q3.inverz().mnozenje_skalarom(36))
print(q3.norma_2())
# print(q2.inverz())
