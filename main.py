import pygame
from pygame.locals import *

from Camera import Camera
from Cube import Cube
from Vector3 import Vector3

from random import randint, uniform

def drawPixel(screen, x, y, r, g, b, WIDTH, HEIGHT):
##    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
##        return
    pygame.draw.circle(screen, (r, g, b), (x, y), 3)
    #surface.set_at((x, y), (r, g, b))

def drawLine(screen, x1, y1, x2, y2, r, g, b, WIDTH, HEIGHT):
##    if (x1 < 0 or x1 >= WIDTH or y1 < 0 or y1 >= HEIGHT
##        or x2 < 0 or x2 >= WIDTH or y2 < 0 or y2 >= HEIGHT):
##        return
    pygame.draw.line(screen, (r, g, b), (x1, y1), (x2, y2))

pygame.init()

WIDTH = 1280
HEIGHT = 720
TICK_RATE = 60

VERTEX_OFFSET = 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 15)
tick = 0

## ----------------------------------------

def createCube(cubeList, cam, colours, rotSpeeds):
    x = uniform(-3, 3)
    y = uniform(-3, 3)
    z = uniform(-5, 0)
    sideLength = uniform(0.5, 2)
    cube = Cube(Vector3(x, y, z), sideLength)

    rotSpeeds.append([uniform(-0.05, 0.05), uniform(-0.05, 0.05), uniform(-0.05, 0.05)])
    colours.append([randint(100, 255), randint(100, 255), randint(100, 255)])

    cubeList.append(cube)
    cam.addObject(cube)

def rotateCubes(cubes, rotSpeeds):
    for i, cube in enumerate(cubes):
        dx = rotSpeeds[i][0]
        dy = rotSpeeds[i][1]
        dz = rotSpeeds[i][2]
        cube.rotate(dx, dy, dz)

cam = Camera(Vector3(-10, 0, 0))
cubeList = list()
colours = list()
rotSpeeds = list()

cubeNum = 3

for i in range(cubeNum):
    createCube(cubeList, cam, colours, rotSpeeds)

## ----------------------------------------

running = True

while running:
    screen.fill((20, 20, 25))

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key in (pygame.K_PLUS, pygame.K_KP_PLUS):
                createCube(cubeList, cam, colours, rotSpeeds)
                cubeNum += 1
            if event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                if len(cubeList) != 0:
                    cubeNum -= 1
                cubeList = cubeList[:-1]
                colours = colours[:-1]
                rotSpeeds = rotSpeeds[:-1]
                cam.objectList = cam.objectList[:-1]

        if event.type == VIDEORESIZE: # Window resize event
            WIDTH = event.w
            HEIGHT = event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    rotateCubes(cubeList, rotSpeeds)

    cubeIndex = 0

    cam.update(WIDTH, HEIGHT)
    for i, vertex in enumerate(cam.getProjectedCoordinates()):
        adjacentVertices = cam.objectList[0].getAdjacentVertices(i % 8)
        for adjacentVertex in adjacentVertices:
            adjacentVertexPos = cam.projectedVertexList[(VERTEX_OFFSET * cubeIndex) + cam.objectList[cubeIndex].tripleIndexer(adjacentVertex)]
            drawLine(
                screen, int(vertex[0]), int(vertex[1]), int(adjacentVertexPos[0]), int(adjacentVertexPos[1]),
                colours[cubeIndex][0], colours[cubeIndex][1], colours[cubeIndex][2], WIDTH, HEIGHT)
        #drawPixel(screen, int(vertex[0]), int(vertex[1]), 250, 100, 100, WIDTH, HEIGHT)
        if i != 0 and (i+1) % 8 == 0:
            cubeIndex += 1

    #lookIntersection = cam.getPixelIntersection(cam.lookDirection, WIDTH, HEIGHT)
    #pygame.draw.circle(screen, (255, 255, 255), list(map(int, lookIntersection)), 10)

    fps_text = font.render("FPS: " + str(round(clock.get_fps(), 1)), 1, (255, 255, 255))
    screen.blit(fps_text, (10, 5))

    counter_text = font.render("Number of cubes: " + str(cubeNum), 1, (255, 255, 255))
    screen.blit(counter_text, (10, 25))

    t = font.render("Use the '+' and '-' keys to add or delete cubes", 1, (255, 255, 255))
    screen.blit(t, (10, 45))

    pygame.display.flip()
    clock.tick(TICK_RATE)
    tick += 1















































