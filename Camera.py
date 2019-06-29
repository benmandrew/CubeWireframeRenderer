import math

from math import cos, sin

from Vector3 import Vector3

class Camera:
    def __init__(self, position):
        self.position = position
        self.lookDirection = Vector3(1, 0, 0)

        self.aspectRatio = 16/9
        self.horizontalFOV = math.pi#0.5 * math.pi
        self.verticalFOV = self.horizontalFOV / self.aspectRatio

        self.objectList = list()
        self.projectedVertexList = list()

    def update(self, pixelWidth, pixelHeight):
        self.calcTopLeftDirection()
        self.calcProjectedVertices(pixelWidth, pixelHeight)

    def calcTopLeftDirection(self):
        self.topLeftDirection = Vector3(self.lookDirection.x, self.lookDirection.y, self.lookDirection.z)
        self.topLeftDirection.rotateX(-(self.horizontalFOV / 2))
        self.topLeftDirection.rotateY((self.verticalFOV / 2))

    def lookAt(self, position):
        difference = position - self.position
        self.lookDirection = difference.normalise()

    def addObject(self, newObject):
        self.objectList.append(newObject)

    def calcProjectedVertices(self, pixelWidth, pixelHeight):
        self.projectedVertexList = list()
        for object_ in self.objectList:
            for vertex in object_.vertexList:
                self.projectedVertexList.append(
                    self.getPixelIntersection(vertex, pixelWidth, pixelHeight))

    def getProjectedCoordinates(self):
        return self.projectedVertexList

    def getPixelIntersection(self, vertexPosition, width, height):
        horizontalAngle = self.getHorizontalAngle(vertexPosition)
        verticalAngle = self.getVerticalAngle(vertexPosition)

        #print(horizontalAngle, "=", horizontalAngle / self.horizontalFOV)

        xPixel = (width * (horizontalAngle / self.horizontalFOV))
        yPixel = (height * (verticalAngle / self.verticalFOV))
        return (xPixel, yPixel)

    def getHorizontalAngle(self, vertexPosition):
        horizontalLookDirection = Vector3(self.topLeftDirection.x, self.topLeftDirection.y, 0)
        horizontalVertexDirection = Vector3(
            vertexPosition.x - self.position.x, vertexPosition.y - self.position.y, 0)#.normalise()

        dotProduct = horizontalLookDirection.dot(horizontalVertexDirection)
        magnitude = horizontalLookDirection.getLength() * horizontalVertexDirection.getLength()
        horizontalAngle = math.acos(dotProduct / magnitude)

        return horizontalAngle

    def getVerticalAngle(self, vertexPosition):
        verticalLookDirection = Vector3(self.topLeftDirection.x, 0, self.topLeftDirection.z)
        verticalVertexDirection = Vector3(
            vertexPosition.x - self.position.x, 0, vertexPosition.z - self.position.z)#.normalise()

        dotProduct = verticalLookDirection.dot(verticalVertexDirection)
        magnitude = verticalLookDirection.getLength() * verticalVertexDirection.getLength()
        verticalAngle = math.acos(dotProduct / magnitude)

        return verticalAngle

    def rotate(self, x):
        newVertex = Vector3(0, 0, 0)
        newVertex.x = self.lookDirection.x * cos(x) - self.lookDirection.y * sin(x)
        newVertex.y = self.lookDirection.x * sin(x) + self.lookDirection.y * cos(x)
        newVertex.z = self.lookDirection.z
        self.lookDirection.copyFrom(newVertex)



































