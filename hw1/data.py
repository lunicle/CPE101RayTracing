class Point():
    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Vector():
    def __init__(self,x,y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

class Ray():
    def __init__(self,pt,dir):
        self.pt = pt
        self.dir = dir

class Sphere():
    def __init__(self,point, radius):
        self.point = point
        self.radius = float(radius)


