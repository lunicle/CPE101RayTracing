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
    def __init__(self,point, radius):
        self.point = point
        self.radius = float(radius)
    def __eq__(self, other):
        return utility.epsilon_equal(self.point, other.point) and utility.epsilon_equal(self.radius, other.radius)