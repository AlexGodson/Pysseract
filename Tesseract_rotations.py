from Linear_algebra import Matrix, Array, cross_multiply
import pygame
from math import pi, cos, sin

## Tesseract

def rotateXY(points, theta):
    for i in range(len(points)):
        rotation_mat = Matrix([
            [cos(theta), -sin(theta), 0, 0],
            [sin(theta), cos(theta), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        points[i] = Matrix(rotation_mat.matrix_cross(matrix_B=points[i]))

def rotateXZ(points, theta):
    for i in range(len(points)):
        rotation_mat = Matrix([
            [cos(theta), 0, -sin(theta), 0],
            [0, 1, 0, 0],
            [sin(theta), 0, cos(theta), 0],
            [0, 0, 0, 1]
        ])
        points[i] = Matrix(rotation_mat.matrix_cross(matrix_B=points[i]))

def rotateXW(points, theta):
    for i in range(len(points)):
        rotation_mat = Matrix([
            [cos(theta), 0, 0, -sin(theta)],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [sin(theta), 0, 0, cos(theta)]
        ])
        points[i] = Matrix(rotation_mat.matrix_cross(matrix_B=points[i]))

def rotateYZ(points, theta):
    for i in range(len(points)):
        rotation_mat = Matrix([
            [1, 0, 0, 0],
            [0, cos(theta), -sin(theta), 0],
            [0, sin(theta), cos(theta), 0],
            [0, 0, 0, 1]
        ])
        points[i] = Matrix(rotation_mat.matrix_cross(matrix_B=points[i]))

def rotateYW(points, theta):
    for i in range(len(points)):
        rotation_mat = Matrix([
            [1, 0, 0, 0],
            [0, cos(theta), 0, -sin(theta)],
            [0, 0, 1, 0],
            [0, sin(theta), 0, cos(theta)]
        ])
        points[i] = Matrix(rotation_mat.matrix_cross(matrix_B=points[i]))

def rotateZW(points, theta):
    for i in range(len(points)):
        rotation_mat = Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, cos(theta), -sin(theta)],
            [0, 0, sin(theta), cos(theta)]
        ])
        points[i] = Matrix(rotation_mat.matrix_cross(matrix_B=points[i]))


## Cube