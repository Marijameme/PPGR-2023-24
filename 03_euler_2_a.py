import numpy as np
from math import cos, sin
from numpy import linalg  #ako vam treba
np.set_printoptions(precision=5, suppress=True)
 
def rotation_z(a):
    return np.array([[cos(a), -sin(a), 0], [sin(a), cos(a), 0], [0, 0, 1]])

def rotation_y(a):
    return np.array([[cos(a), 0, sin(a)], [0, 1, 0], [-sin(a), 0, cos(a)]])

def rotation_x(a):
    return np.array([[1, 0, 0], [0, cos(a), -sin(a)], [0, sin(a), cos(a)]])
 
def Euler2A(uglovi):
    Rz = rotation_z(uglovi[0])
    Ry = rotation_y(uglovi[1])
    Rx = rotation_x(uglovi[2])

    A = np.dot(np.dot(Rz, Ry), Rx)
 
    A = np.where(np.isclose(A, 0) , 0 , A)  # da bi izbegli -0. u rezultatu
    return A
 
# uglovi = np.array([np.pi/2, -np.pi/4, (7/8)*np.pi])
# print(Euler2A(uglovi))