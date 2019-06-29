import math

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector3(x, y, z)

    def __mul__(self, other):
        return Vector3(other * self.x, other * self.y, other * self.z)

    def __str__(self):
        return "[{0}, {1}, {2}]".format(self.x, self.y, self.z)

    def __repr__(self):
        return "[{0}, {1}, {2}]".format(self.x, self.y, self.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def getLength(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def normalise(self):
        magnitude = self.getLength()
        x = self.x / magnitude
        y = self.y / magnitude
        z = self.z / magnitude
        return Vector3(x, y, z)

    def rotate(self, x, y, z):
        if x != 0: self.rotateX(x)
        if y != 0: self.rotateY(y)
        if z != 0: self.rotateZ(z)

    def rotateX(self, x):
        newVertex = Vector3(0, 0, 0)
        newVertex.x = self.x * math.cos(x) - self.y * math.sin(x)
        newVertex.y = self.x * math.sin(x) + self.y * math.cos(x)
        newVertex.z = self.z
        self.copyFrom(newVertex)

    def rotateY(self, y):
        newVertex = Vector3(0, 0, 0)
        newVertex.x = self.x * math.cos(y) + self.z * math.sin(y)
        newVertex.y = self.y
        newVertex.z = -self.x * math.sin(y) + self.z * math.cos(y)
        self.copyFrom(newVertex)

    def rotateZ(self, z):
        newVertex = Vector3(0, 0, 0)
        newVertex.x = self.x
        newVertex.y = self.y * math.cos(z) - self.z * math.sin(z)
        newVertex.z = self.y * math.sin(z) + self.z * math.cos(z)
        self.copyFrom(newVertex)

    def copyFrom(self, other):
        self.x = other.x
        self.y = other.y
        self.z = other.z

















