import utility

class Point():
    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y, other.y) and utility.epsilon_equal(self.z, other.z)
    def __repr__(self):
        return "(" + str(self.x) +", " + str(self.y) + ", " + str(self.z) + ")"
class Vector():
    def __init__(self,x,y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y, other.y) and utility.epsilon_equal(self.z, other.z)

class Ray():
    def __init__(self,pt,dir):
        self.pt = pt
        self.dir = dir
    def __eq__(self, other):
        return utility.epsilon_equal(self.pt, other.pt) and utility.epsilon_equal(self.dir, other.dir)

class Sphere():
    def __init__(self,point,radius,color,finish):
        self.point = point
        self.radius = float(radius)
        self.color = color
        self.finish = finish
    def __eq__(self, other):
        return utility.epsilon_equal(self.point, other.point) and utility.epsilon_equal(self.radius, other.radius) and utility.epsilon_equal(self.color, other.color) and utility.epsilon_equal(self.ambient, other.ambient)

class Color():
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
    def __eq__(self,other):
        return utility.epsilon_equal(self.r, other.r) and utility.epsilon_equal(self.g, other.g) and utility.epsilon_equal(self.b, other.b)

class Finish():
    def __init__(self,ambient,diffuse):
        self.ambient = float(ambient)
        self.diffuse = diffuse
    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient, other.ambient) and utility.epsilon_equal(self.diffuse, other.diffuse)

class Light():
    def __init__(self, pt, color):
        self.pt = pt
        self.color = color
    def __eq__(self,other):
        return utility.epsilon_equal(self.pt, other.pt) and utility.epsilon_equal(self.color, other.color)