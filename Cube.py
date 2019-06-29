from math import cos, sin

from Vector3 import Vector3

class Cube:
    def __init__(self, position, sideLength):
        self.position = position
        self.sideLength = sideLength

        self.vertexList = list()
        self.generateVertices()

    def generateVertices(self):
        self.vertexList = list()
        positionalModifiers = (
            Vector3(1, 1, 1), Vector3(1, 1, -1),
            Vector3(1, -1, 1), Vector3(1, -1, -1),
            Vector3(-1, 1, 1), Vector3(-1, 1, -1),
            Vector3(-1, -1, 1), Vector3(-1, -1, -1))
        for positionalModifier in positionalModifiers:
            newVertex = self.position + (positionalModifier * (self.sideLength / 2.0))
            self.vertexList.append(newVertex)

    def rotate(self, x, y, z):
        if x != 0: self.rotateX(x)
        if y != 0: self.rotateY(y)
        if z != 0: self.rotateZ(z)

    def rotateX(self, x):
        for i, vertex in enumerate(self.vertexList):
            newVertex = Vector3(0, 0, 0)
            newVertex.x = vertex.x * cos(x) - vertex.y * sin(x)
            newVertex.y = vertex.x * sin(x) + vertex.y * cos(x)
            newVertex.z = vertex.z
            self.vertexList[i] = newVertex

    def rotateY(self, y):
        for i, vertex in enumerate(self.vertexList):
            newVertex = Vector3(0, 0, 0)
            newVertex.x = vertex.x * cos(y) + vertex.z * sin(y)
            newVertex.y = vertex.y
            newVertex.z = -vertex.x * sin(y) + vertex.z * cos(y)
            self.vertexList[i] = newVertex

    def rotateZ(self, z):
        for i, vertex in enumerate(self.vertexList):
            newVertex = Vector3(0, 0, 0)
            newVertex.x = vertex.x
            newVertex.y = vertex.y * cos(z) - vertex.z * sin(z)
            newVertex.z = vertex.y * sin(z) + vertex.z * cos(z)
            self.vertexList[i] = newVertex

    def tripleIndexer(self, index):
        return index[0] * 4 + index[1] * 2 + index[2]

    def tripleIndexInverse(self, index):
        inverse = bin(index)[2:]
        while len(inverse) < 3:
            inverse = "0" + inverse
        return list(map(int, inverse))

    def getAdjacentVertices(self, index):
        tripleIndex = self.tripleIndexInverse(index)
        modifiers = [
            [1, 0, 0], [-1, 0, 0],
            [0, 1, 0], [0, -1, 0],
            [0, 0, 1], [0, 0, -1]]
        adjacentVertices = list()
        for modifier in modifiers:
            moddedTriple = addList(tripleIndex, modifier)
            if not tripleOutsideBounds(moddedTriple, 2):
                adjacentVertices.append(moddedTriple)
        return adjacentVertices

def addList(list1, list2):
    return [x+y for x, y in zip(list1, list2)]

def tripleOutsideBounds(tripleIndex, bound):
    if not (0 <= tripleIndex[0] < bound and
            0 <= tripleIndex[1] < bound and
            0 <= tripleIndex[2] < bound):
        return True
    return False

##c = Cube(Vector3(0, 0, 0), 1)
##for i in range(8):
##    v = c.tripleIndexInverse(i)
##    x = c.tripleIndexer(v)
##    print(x, v)





















