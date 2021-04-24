from math import sqrt, pow

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2) )

    def __add__(self, b):
        if type(b) is Vector3:
            return Vector3(self.x + b.x, self.y + b.y, self.z + b.z)
        elif type(b) is Vector2:
            return Vector3(self.x + b.x, self.y + b.x, self.z)
        else:
            return Vector3(self.x + b, self.y + b, self.z + b)

    def __sub__(self, b):
        if type(b) is Vector3:
            return Vector3(self.x - b.x, self.y - b.y, self.z - b.z)
        elif type(b) is Vector2:
            return Vector3(self.x - b.x, self.y - b.y, self.z)
        else:
            return Vector3(self.x - b, self.y - b, self.z - b)

    def __mul__(self, b):
        if type(b) is Vector3:
            return Vector3(self.x * b.x, self.y * b.y, self.z * b.z)
        return Vector3(self.x * b, self.y * b, self.z * b)

    def __truediv__(self, b):
        if type(b) is Vector3:
            return Vector3(self.x / b.x, self.y / b.y, self.z / b.z)
        return Vector3(self.x / b, self.y / b, self.z / b)


    def __repr__(self):
        return f'{self.x} , {self.y}, {self.z}'

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
        return Vector2(self.x / b, self.y / b)

    def TuplePosition(self):
        return (int(self.x), int(self.y))

    def __repr__(self):
        return f'{self.x} , {self.y}'

def Distance(v1, v2):
    if type(v1) is Vector2 :
        return sqrt( (v1.x - v2.x)*(v1.x - v2.x) + (v1.y - v2.y)*(v1.y - v2.y) )
    elif type(v1) is Vector3 :
        return sqrt( (v1.x - v2.x) *(v1.x - v2.x) + (v1.y - v2.y)*(v1.y - v2.y) + (v1.z - v2.z)*(v1.z - v2.z))
