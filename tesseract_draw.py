import pygame
from Linear_algebra import *

white = (255, 255, 255)

colour = white

def draw_shape(points, canvas, lin_width):
    for i in range(4):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[(i+1)%4].matrix[0][0]+200, points[(i+1)%4].matrix[1][0]+200)
        pygame.draw.line(canvas, colour, start_pos, end_pos, lin_width)
    for i in range(4, 8):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[(i+1)%4+4].matrix[0][0]+200, points[(i+1)%4+4].matrix[1][0]+200)
        pygame.draw.line(canvas, colour, start_pos, end_pos, lin_width)
    for i in range(4):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[i+4].matrix[0][0]+200, points[i+4].matrix[1][0]+200)
        pygame.draw.line(canvas, colour, start_pos, end_pos, lin_width)
    for i in range(8,12):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[(i+1)%4+8].matrix[0][0]+200, points[(i+1)%4+8].matrix[1][0]+200)
        pygame.draw.line(canvas, colour, start_pos, end_pos, lin_width)
    for i in range(4):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[i+8].matrix[0][0]+200, points[i+8].matrix[1][0]+200)
        pygame.draw.line(canvas, colour, start_pos, end_pos, lin_width)
    for i in range(8,12):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[(i+4)].matrix[0][0]+200, points[(i+4)].matrix[1][0]+200)
        pygame.draw.line(canvas, colour, start_pos, end_pos, lin_width)
    for i in range(12,16):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[(i+1)%4+12].matrix[0][0]+200, points[(i+1)%4+12].matrix[1][0]+200)
        pygame.draw.line(canvas, colour, start_pos, end_pos, lin_width)
    for i in range(4,8):
        start_pos = (points[i].matrix[0][0]+200, points[i].matrix[1][0]+200)
        end_pos = (points[(i+8)].matrix[0][0]+200, points[(i+8)].matrix[1][0]+200)
        pygame.draw.line(canvas, colour, start_pos, end_pos, lin_width)