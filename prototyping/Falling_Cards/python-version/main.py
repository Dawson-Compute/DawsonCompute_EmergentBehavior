import pygame
from math import cos, sin
from pygame import Vector3, Vector2


def rotate2D(point, angle):
    c = cos(angle)
    s = sin(angle)
    return [c*point.x - s*point.y, s*point.x +c*point.y]
def rotate_x(point, angle):
    p = Vector2(point.y, point.z)
    rp = rotate2D(p, angle)
    return Vector3(point.x, rp.y, rp.z)

def rotate_y(point, angle):
    p = Vector2(point.y, point.z)
    rp = rotate2D(p, angle)
    return Vector3(point.x, rp.y, rp.z)

def rotate_z(point, angle):
    p = Vector2(point.y, point.z)
    rp = rotate2D(p, angle)
    return Vector3(point.x, rp.y, rp.z)



def transform(point, ori):


class Camera:
    def __init__(self):
        self.pos = Vector3()
    
    def project(self, point : Vector3):
        return (point.x / abs(point.z), point.y / (point.z))

## We can approximate depth = 0?
class Card:
    def __init__(self, size, position, orientation):
        self.dims = size 
        self.pos = position
        self.ori = orientation
        self.vel = Vector3()
        self.avel = Vector3()

    def update(self,dt):
        self.pos += self.vel * dt 
        self.ori += self.avel * dt

    def display(self, camera):
        points = []

