from Linear_algebra import Matrix, Array, cross_multiply
import pygame
from Tesseract_rotations import *
from math import pi, cos, sin
from tesseract_draw import *

pygame.init()

FPS = 50

Window_scale = 2
WIDTH, HEIGHT = 400, 400
WIDTH_SCALED = WIDTH * Window_scale
HEIGHT_SCALED = HEIGHT * Window_scale

lin_width = 3
depth = 1

black = (0, 0, 0)
white = (255, 255, 255)

def isometric_4to3(points):
    distance = 120
    projected_points = []
    for point in points:
        scale = distance / (distance - point.matrix[-1][0])
        isometric_mat = Matrix([
            [scale, 0, 0, 0],
            [0, scale, 0, 0],
            [0, 0, scale, 0]
        ])
        projected_points.append(Matrix(isometric_mat.matrix_cross(point)))
    return projected_points

def isometric_3to2(points):
    distance = 200
    projected_points = []
    for point in points:
        scale = distance / (distance - point.matrix[-1][0])
        isometric_mat = Matrix([
            [scale, 0, 0],
            [0, scale, 0],
        ])
        projected_points.append(Matrix(isometric_mat.matrix_cross(point)))
    return projected_points

def update_win(canvas, window, points):
    canvas.fill(black)
    projected_points = isometric_4to3(points=points)
    # projected_points = isometric_3to2(points=projected_points)
    draw_shape(projected_points, canvas, lin_width=lin_width)
    for point in projected_points:
        coords = (point.matrix[0][0]+200, point.matrix[1][0]+200)
        pygame.draw.circle(canvas, white, coords, 1)
    window.blit(pygame.transform.scale(canvas, (WIDTH_SCALED, HEIGHT_SCALED)), (0, 0))
    pygame.display.update()


def main():
    running = True
    clock = pygame.time.Clock()
    CANVAS = pygame.Surface((WIDTH, HEIGHT))
    WINDOW = pygame.display.set_mode((WIDTH_SCALED, HEIGHT_SCALED))

    POINTS = []
    # Defined points = [ [x], [y], [z], [w] ]
    POINTS.append(Matrix([ [60], [60], [60], [60] ]))   # 0
    POINTS.append(Matrix([ [-60], [60], [60], [60] ]))  # 1
    POINTS.append(Matrix([ [-60], [-60], [60], [60] ])) # 2
    POINTS.append(Matrix([ [60], [-60], [60], [60] ]))  # 3
    POINTS.append(Matrix([ [60], [60], [-60], [60] ]))  # 4
    POINTS.append(Matrix([ [-60], [60], [-60], [60] ])) # 5
    POINTS.append(Matrix([ [-60], [-60], [-60], [60] ]))# 6
    POINTS.append(Matrix([ [60], [-60], [-60], [60] ])) # 7
    POINTS.append(Matrix([ [60], [60], [60], [-60] ]))  # 8
    POINTS.append(Matrix([ [-60], [60], [60], [-60] ])) # 9
    POINTS.append(Matrix([ [-60], [-60], [60], [-60] ]))# 10
    POINTS.append(Matrix([ [60], [-60], [60], [-60] ])) # 11
    POINTS.append(Matrix([ [60], [60], [-60], [-60] ])) # 12
    POINTS.append(Matrix([ [-60], [60], [-60], [-60] ]))# 13
    POINTS.append(Matrix([ [-60], [-60], [-60], [-60] ]))#14 
    POINTS.append(Matrix([ [60], [-60], [-60], [-60] ]))# 15 


    # POINTS = rotateXW(points=POINTS, theta=pi)

    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            running = False
            break

        # points = rotateXY(points=POINTS, theta=0.005)
        # points = rotateXZ(points=POINTS, theta=0.003)
        points = rotateXW(points=POINTS, theta=0.003)
        # points = rotateYZ(points=POINTS, theta=0.005)
        # points = rotateYW(points=POINTS, theta=0.005)
        points = rotateZW(points=POINTS, theta=0.008)
        

        update_win(canvas=CANVAS, window=WINDOW, points=POINTS)
        # theta = +0.0005

if __name__ == "__main__":
    main()