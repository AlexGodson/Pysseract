from Linear_algebra import Matrix, Array, cross_multiply
import pygame
from math import pi, cos, sin

pygame.init()

FPS = 60

Window_scale = 2
WIDTH, HEIGHT = 400, 400
WIDTH_SCALED = WIDTH * Window_scale
HEIGHT_SCALED = HEIGHT * Window_scale

black = (0, 0, 0)
white = (255, 255, 255)

def draw_shape(points, canvas):
    for i in range(4):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[(i+1)%4].matrix[0][0]+200, points[(i+1)%4].matrix[1][0]+200)
        pygame.draw.line(canvas, white, start_pos, end_pos)
    for i in range(4, 8):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[(i+1)%4+4].matrix[0][0]+200, points[(i+1)%4+4].matrix[1][0]+200)
        pygame.draw.line(canvas, white, start_pos, end_pos)
    for i in range(4):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[i+4].matrix[0][0]+200, points[i+4].matrix[1][0]+200)
        pygame.draw.line(canvas, white, start_pos, end_pos)
    return canvas

def stereographic_proj(points):
    distance = 400
    projected_points = []
    for point in points:
        scale = distance / (distance-point.matrix[-1][0])
        projection_matrix = Matrix([
            [scale, 0, 0],
            [0, scale, 0]
        ])
        projected_points.append(Matrix(projection_matrix.matrix_cross(point)))
    return projected_points

def update_win(canvas, window, points):
    projected_points = stereographic_proj(points)
    canvas.fill(black)
    draw_shape(projected_points, canvas)
    for point in projected_points:
        coords = (point.matrix[0][0]+200, point.matrix[1][0]+200)
        # point = pygame.draw.circle(canvas, white, coords, 1)
    window.blit(pygame.transform.scale(canvas, (WIDTH_SCALED, HEIGHT_SCALED)), (0, 0))
    pygame.display.update()

def rotateZ(points, theta=0):
    for i in range(len(points)):
        rotation_mat = Matrix([
            [cos(theta), -sin(theta), 0],
            [sin(theta), cos(theta), 0],
            [0, 0, 1]
        ])
        points[i] = Matrix(rotation_mat.matrix_cross(matrix_B=points[i]))

def rotateX(points, theta):
    for i in range(len(points)):
        rotation_mat = Matrix([
            [1, 0, 0],
            [0, cos(theta), -sin(theta)],
            [0, sin(theta), cos(theta)]
        ])
        points[i] = Matrix(rotation_mat.matrix_cross(matrix_B=points[i]))

def rotateY(points, theta):
    for i in range(len(points)):
        rotation_mat = Matrix([
            [cos(theta), 0, sin(theta)],
            [0, 1, 0],
            [-sin(theta), 0, cos(theta)]
        ])
        points[i] = Matrix(rotation_mat.matrix_cross(matrix_B=points[i]))

def main():
    running = True
    clock = pygame.time.Clock()
    CANVAS = pygame.Surface((WIDTH, HEIGHT))
    WINDOW = pygame.display.set_mode((WIDTH_SCALED, HEIGHT_SCALED))

    POINTS = []
    # Defined points = [ [x], [y], [z], [w], [v] ]
    POINTS.append(Matrix([ [-100], [100], [100] ]))
    POINTS.append(Matrix([ [100], [100], [100] ]))
    POINTS.append(Matrix([ [100], [-100], [100] ]))
    POINTS.append(Matrix([ [-100], [-100], [100] ]))
    POINTS.append(Matrix([ [-100], [100], [-100] ]))
    POINTS.append(Matrix([ [100], [100], [-100] ]))
    POINTS.append(Matrix([ [100], [-100], [-100] ]))
    POINTS.append(Matrix([ [-100], [-100], [-100] ]))

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

        rotateX(points=POINTS, theta=0.005)
        rotateZ(points=POINTS, theta=0.01)
        # rotateY(points=POINTS, theta=theta)
        update_win(canvas=CANVAS, window=WINDOW, points=POINTS)

if __name__ == "__main__":
    main()