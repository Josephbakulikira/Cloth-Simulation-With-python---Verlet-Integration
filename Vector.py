from math import sqrt, pow
from constants import *

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def __add__(self, b):
        if type(b) is Vector2:
            return Vector2(self.x + b.x, self.y + b.y)
        return Vector2(self.x + b, self.y + b)

    def __sub__(self, b):
        if type(b) is Vector2:
            return Vector2(self.x - b.x, self.y - b.y)
        return Vector2(self.x - b, self.y - b)

    def __mul__(self, b):
        if type(b) is Vector2:
            return Vector2(self.x * b.x, self.y * b.y)
        return Vector2(self.x * b, self.y * b)

    def __truediv__(self, b):
        if type(b) is Vector2:
            return Vector2(self.x / b.x, self.y / b.y)
        if b == 0:
            return Vector2(0, 0)
        return Vector2(self.x / b, self.y / b)

    def TuplePosition(self):
        x, y =self.x, self.y
        if self.x > Width:
            x = Width
        elif self.x < 0:
            x = 0

        if self.y > Height:
            y = Height
        if self.y < 0:
            y = 0
        return (x, y)

    def __repr__(self):
        return f'{self.x} , {self.y}'

def toVector(mat):
    if len(mat) == 2:
        return Vector2(mat[0][0], mat[1][0])
    else:
        return Vector3(mat[0][0], mat[1][0], mat[2][0])
def Distance(v1, v2):
    if type(v1) is Vector2 :
        return sqrt( (v1.x - v2.x)*(v1.x - v2.x) + (v1.y - v2.y)*(v1.y - v2.y) )
    elif type(v1) is Vector3 :
        return sqrt( (v1.x - v2.x) *(v1.x - v2.x) + (v1.y - v2.y)*(v1.y - v2.y) + (v1.z - v2.z)*(v1.z - v2.z))
